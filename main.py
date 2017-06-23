#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 11:04:28 2017
@author: mulang
"""
from query import queryProc
from practnlptools.tools import Annotator
from predicates import predicates
from utils import similarity as sim
#from time import gmtime, strftime

def process_query(query):
    annotator=Annotator()
    annotations = annotator.getAnnotations(query,dep_parse=True)
    (bag_of_words,pos_seq,ner_seq,chunk_seq,dep_seq,srls) = queryProc.extract_annotations(annotations)
    last_pos = len(bag_of_words) - 1    
   
    bin_rels = queryProc.recursive_binaries(bag_of_words,pos_seq,ner_seq,chunk_seq,dep_seq,last_pos)
    
    clean_rels = []
    prev_rel_heads = ""
    
    for rel in bin_rels :
        if str(rel.head).strip(" ") in prev_rel_heads.split(" ") :
            continue
        else :
            prev_rel_heads  = prev_rel_heads + " " +rel.head
            clean_rels.append(rel)            
        
    return clean_rels, bag_of_words 

def main():
        
    all_props = predicates.get_AllKBproperties()
    #bin_rels, bag_of_words=process_query("How many people live in the Capital of Australia?")
    #bin_rels, bag_of_words=process_query("Who is the wife of Barack Obama?")
    #bin_rels, bag_of_words=process_query("Who wrote the book Harry Porter?")
    bin_rels, bag_of_words=process_query("Give me all people that were born in Vienna and died in Berlin")
    
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
    #EVALUATION CODE
    
    #end_time =start_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    #print "\n\n",start_time,"\n\n"
    #print "\n\n",end_time,"\n\n"
    '''all_props = predicates.get_AllKBproperties()
     
    datasets_file = "auto_queries.csv"
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
        
        #with open(test_outputs) as out_file :'''
            
            
if __name__== "__main__":
  main()