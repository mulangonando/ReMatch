#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 11:04:28 2017
@author: mulang
"""
from query import queryProc
from practnlptools.tools import Annotator
from predicates.predicates import KBproperty
from utils import similarity as sim
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import gc
import os
import csv
import time
import SocketServer
import json
import gc, sys
import cPickle as pic
#from time import gmtime, strftime

proj_dir = os.path.abspath(os.path.join('.'))
binaries_dir = os.path.abspath(os.path.join('.','DBPedia','onto_binaries'))
sys.path.append(proj_dir)
dbpedia_prop = os.path.abspath(os.path.join(binaries_dir,"prop"))
rels_file = os.path.abspath(os.path.join('DBPedia','rel_words'))

all_props = []
requests = 0

def process_query(query):
    
    gazzet_file = os.path.abspath(os.path.join('.','Gazetteer','country_names.csv'))
    countries_list = []

    with open(gazzet_file) as c:
        countries = csv.reader(c)
   
        for row in countries:
            countries_list.append(row[0].lower())
            countries_list.append(row[1].lower())
            countries_list.append(row[2].lower())
    
    query = query.replace("-"," ")
    
    '''for word in query_words:
        
        if word.lower() in countries_list:
            query = query.replace(word,"country")
            print word'''
            
    global requests 
    annotator = Annotator()
    annotations = annotator.getAnnotations(query,dep_parse=True)
    
    (bag_of_words,pos_seq,ner_seq,chunk_seq,dep_seq,srls) = queryProc.extract_annotations(annotations)
    
    last_pos = len(bag_of_words) - 1    

    bin_rels = queryProc.recursive_binaries(bag_of_words,pos_seq,ner_seq,chunk_seq,dep_seq,last_pos,binaries=[], sent_words = [])
    
    rels = bin_rels #[:(len(bin_rels)-requests)+1]
    
    requests = len(bin_rels)

    clean_rels = []
    prev_rel_heads = ""
    
    for rel in rels :
        if str(rel.head).strip(" ") in prev_rel_heads.split(" ") :
            continue
        else :
            prev_rel_heads  = prev_rel_heads + " " +rel.head
            clean_rels.append(rel) 
            
    annotator=None
    annotations = None
    bag_of_words #= None
    pos_seq = None
    ner_seq = None
    chunk_seq = None
    dep_seq = None
    #srls = None
    last_pos = None
    gc.collect()
    return clean_rels, bag_of_words 

        
def get_AllKBproperties():
    global KBproperty
    #fileObject = open(dbpedia_binaries,'r')  
    dbpedia_props = []
    
    file_names = []
    for file in os.listdir(binaries_dir):
        if file.endswith(".pkl"):
            file_names.append(os.path.join(binaries_dir, file))
    
    for name in file_names :
        
        with open(name, "rb") as f:
            kb_prop = KBproperty()
            kb_prop = pic.load(f)
            dbpedia_props.append( kb_prop )
            
            print kb_prop.prop_uri
            #print dbpedia_props(0)
            f.close()
    
    return dbpedia_props

'''
def main():
    start = time.time()   
    all_props = predicates.get_AllKBproperties()
    
    
    
    bin_rels, bag_of_words=process_query("Which actress starring in the TV series Friends owns the production company Coquette Productions?")
     
    
    j=0
    for relation in bin_rels :
        
        weights,uri = sim.top_similar(all_props, relation, bag_of_words) 
        
        k=0
        for word in bag_of_words :
            if word.strip() == relation.head.strip():
                del bag_of_words[k]
            k = k+1
            
        print "Relation ", j+1 , relation.head, " : \n"        
        
        for i in range(len(weights)):            
            print str(weights[i])+" : "+uri[i]+"\n"
 
        j=j+1
    
    stop = time.time()
    #delta = stop - start
    print  stop - start #'#"Time in the Recursive Function : ",delta.total_seconds()
            
if __name__== "__main__":
  main()

    #EVALUATION CODE
    
    #end_time =start_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    #print "\n\n",start_time,"\n\n"
    #print "\n\n",end_time,"\n\n"
'''
all_props = get_AllKBproperties()
     
'''    datasets_file = "auto_queries.csv"
    test_outputs= "test_outputs"
    
    #LOAD THE CSV FILE HERE
    with open(datasets_file) as f:
        queries_data = csv.reader(f)
    
        all_eval = ""
        starter = 1
        for line in queries_data:
            if starter > 110 :
                #    break
                question = line[0]
                len_line = len(line)
                print "NOW THE CURRENT QUESTION : ", question
                Susanne Wandersee
                curr_eval = ""
                bin_rels, bag_of_words=process_query(question) 
                j=0
                for relation in bin_rels :
                    print "DESIRE : ",relation.desire,relation.helper," ",relation.head, relation.non_ent_nouns, 'Right : ', relation.right," Left :  ",relation.left
                    
                    weights,uri = sim.top_similar(all_props, relation, bag_of_words) #,count_attribs, label_attribs,
                    
                    for i in range(len(weights)):
                        print str(weights[i])+" : "+uri[i]+"\n"#
                                    
                        #CHANGE THIS TO ADAPT THE LENTH OF THE LINE
                        #added
                        for k in range(1 , len_line) :
                            print "The Current Rel is : ",uri[i].split("/")[-1] 
                            print "The line : : ", line[k]
                            
                            if uri[i].split("/")[-1] == line[k] :
                                curr_eval = curr_eval+","+str(k)+":"+str(i+1)
                            
                        #curr_eval = curr_eval+","+str(k)+":0"
        
                    del relation
                    del weights
                    del uri
                    gc.collect()
                    j=j+1
    
                    #print curr_eval
                    curr_eval = curr_eval + "\n"
                    fileObject = open(test_outputs,'a')
                    fileObject.write(curr_eval)
                    fileObject.close()
            
                    all_eval = all_eval + "\n"+curr_eval
            
                    print curr_eval
                    bin_rels=[]
            
                del question
                del len_line
                del bin_rels
                del curr_eval
                #del line
                gc.collect()
                
            #gc.collect()
            
            starter = starter + 1
'''        
        #with open(test_outputs) as out_file :            
class S(BaseHTTPRequestHandler):
    
    def _init_(self):
        global all_props
         
        
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>hi!</h1></body></html>")

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        global all_props
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        #print "Post Data : ",post_data
        bin_rels = []
        bin_rels, bag_of_words=process_query(post_data)
        del post_data
        j=0
        
        data_dict ={}

        for relation in bin_rels :
            #print relation.head.strip()
            weights,uri = sim.top_similar(all_props, relation, bag_of_words) 
            
            #self.wfile.write(uri)
            
            k=0
            
            #label = ""
            for word in bag_of_words :
                if word.strip() == relation.head.strip():
                    del bag_of_words[k]
                k = k+1
                
            #self.wfile.write("Relation "+ str(j+1) + relation.head+ " : \n" )       
            #self.wfile.write("Your Question : "+post_data) # <-- Print post data
            self._set_headers()      
           
            value = {}
            value_lists = []
            
            for i in range(len(weights)): 
                value_lists.append(uri[i])
                value_lists.append(weights[i])
                
            value[j] = value_lists

            #data.append("Relation "+ str(j+1))
            #data.append(value)
            data_dict[relation.head.strip()]=value
            
            #bin_rels.remove(relation)
            
            j=j+1
        
        json_data = json.dumps(data_dict)
        self.wfile.write(json_data)
        
        bin_rels = None
        relation = None
        bag_of_words = None
        gc.collect()

def run(server_class=HTTPServer, handler_class=S, port=8081):
    global all_props
    #all_props = predicates.get_AllKBproperties()
    #print len(all_props)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()
    

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()