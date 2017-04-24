#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 10:25:34 2017

@author: mulang
"""

import cPickle as pickle
import re
import os, sys
#proj_dir = os.path.abspath(os.path.join('..'))
#binaries_dir = os.path.abspath(os.path.join("..",'DBPedia','binaries'))

proj_dir = os.path.abspath(os.path.join('.'))
binaries_dir = os.path.abspath(os.path.join('DBPedia','binaries'))
print proj_dir
sys.path.append(proj_dir)
dbpedia_prop = os.path.abspath(os.path.join(binaries_dir,"prop"))
#sys.path.append(dbpedia_dir)

from practnlptools.tools import Annotator
import csv
from utils import strings

annotator=Annotator()
annotations = annotator.getAnnotations("currency code",dep_parse=True)

#HERE CREATE A CLASS OF PREDICATE : TO REP A PREDICATE AND ALL IT'S ATTRIBUTES

#PROCESSS THE FILES
class KBproperty(object):
    def __init__(self):
        self.prop_uri = ""
        self.domain = ""
        self.range = ""
        self.label = ""
        self.comment = ""
        self.instances_count = ""
        self.annotations = None
        
        
            
def extract_annotations(annotations):
    srls = annotations['srl']
    poss = annotations['pos']
    ners = annotations['ner']
    chunks = annotations['chunk']
    dep_parse = annotations['dep_parse']
         
    bag_of_words = []
    pos_seq = []
    ner_seq = []
    chunk_seq = []
    dep_seq = []
    for pos in poss :
        bag_of_words.append(pos[0])
        pos_seq.append(pos[1])
    
    for ner in ners :
        ner_seq.append(ner[1])
    
    for chunk in chunks :
        chunk_seq.append(chunk[1])
   
        
    for dep in dep_parse.split('\n') :
        positions = []
        dep_rel = str(dep)[:dep.index("(")]
        pair = dep[dep.index('(')+1:dep.index(')')]
        word1,word2= pair.split(',')
        
        word1_num=word1.split('-')
        word2_num=word2.split('-')
       
        positions.append(dep_rel)
        positions.append(word1_num[1])
        positions.append(word2_num[1])      
        #print quard
        dep_seq.append(positions)    
    return (bag_of_words,pos_seq,ner_seq,chunk_seq,dep_seq,srls)


def file_processor() :
    #pred_file = "DBPedia/DBPedia_predicates"
    pred_file = os.path.join(proj_dir,"DBPedia","DBPedia_pred_counts")
    
    kb_prop = KBproperty()
    all_props = []
    #ORDER OF THE ITEMS : "property","domain","range","label","comment",count
    with open(pred_file) as f:
        predicates = csv.reader(f)
        i = 0
        for row in predicates:
            if len(row) > 6:
                j=4
                while j<len(row) - 2 :
                    row[4] = row[4]+row[j+1]
                    j=j+1
                row[5] =  row[-1]
            pred_uri = row[0]
            kb_prop.prop_uri = pred_uri
            
            domain_word = strings.split_string_on_caps(row[1].split("/")[-1].replace("'",""))
            
            kb_prop.domain = domain_word
            
            range_word = strings.split_string_on_caps(row[2].split("/")[-1].split("#")[-1].replace("'",""))
           
            kb_prop.range = range_word
            
            pred_label = row[3].strip()
            pred_label = re.sub(r"^'|'$", "", pred_label)
            pred_label = pred_label.replace("(","")
            pred_label = pred_label.replace(")","")
           
            kb_prop.label = pred_label
            
            count = row[-1]
                                    
            kb_prop.instances_count = count
            
            #HERE WE SHIFT THE LABESLS THAT ARE REALY JUST COMMENTS AND GENERATE NEW LABELS
            if (len(row[0].split("/")[-1]) < (len(pred_label) - len(pred_label.split(' '))) and pred_label.find("(")==-1) :
                row[4] = pred_label
                row[3] = row[0].split("/")[-1]
                pred_label = strings.split_string_on_caps(row[3].replace("'",""))        
            
            comment =row[4].replace('(','').replace(')','').strip()
            comment =  re.sub(r"^'|'$", "", comment)
            comment =  re.sub(r'^"|"$', '', comment)
                        
            kb_prop.comment = comment
                        
            sentence = domain_word.strip(" ")+ " "+pred_label.strip(" ")+ " "+  range_word.strip(" ")
            if len(comment)>0 :
                sentence = sentence+" "+ comment
            
            sentence.replace("(","")
            annotator=Annotator()
            prop_ann = annotator.getAnnotations(sentence,dep_parse=True)
        
            bag_of_words,pos_seq,ner_seq,chunk_seq,dep_seq,srls = extract_annotations(prop_ann) 
        
            kb_prop.annotations = {}
            kb_prop.annotations["bag_of_words"] = bag_of_words
            kb_prop.annotations["pos_seq"] = pos_seq
            kb_prop.annotations["ner_seq"] = ner_seq
            kb_prop.annotations["chunk_seq"] = chunk_seq
            kb_prop.annotations["dep_seq"] = dep_seq
            kb_prop.annotations["srls"] = srls
                                    
            ##all_props.append(kb_prop)
                        
            #if i==10 :
            #    break             
            
            with open(dbpedia_prop+"_"+str(i)+".pkl", "wb") as data_file:
                pickle.dump(kb_prop, data_file)
                data_file.close
            
            i=i+1
        #fileObject = open(dbpedia_binaries,'wb') 
        #pickle.dump(all_props,fileObject) 
        #fileObject.close()
        
        
        f.close()

def get_AllKBproperties():
    
    #fileObject = open(dbpedia_binaries,'r')  
    dbpedia_props = []
    file_names = []
    for file in os.listdir(binaries_dir):
        if file.endswith(".pkl"):
            file_names.append(os.path.join(binaries_dir, file))
    
    for name in file_names :
        
        with open(name, "rb") as f:
            dbpedia_props.append(pickle.load(f) )
            
            f.close()
    
    return dbpedia_props

#get_AllKBproperties()           
#file_processor()


all_props = get_AllKBproperties()
print all_props[0].prop_uri, all_props[1].prop_uri
#print all_props[2].prop_uri, all_props[3].prop_uri
#print all_props[4].prop_uri, all_props[5].prop_uri
#print all_props[6].prop_uri, all_props[7].prop_uri
#print all_props[8].prop_uri, all_props[9].prop_uri
#print all_props[10].prop_uri, all_props[11].prop_uri
#j=0
#for prop in all_props:
    
#    prop.prop_uri
#    prop.domain
#    prop.range
#    prop.label
#    prop.comment
#    prop.instances_count
#    prop.annotations['bag_of_words']
#    print "\n\n"
#    if j==10:
#        break
#    j = j+1
    
