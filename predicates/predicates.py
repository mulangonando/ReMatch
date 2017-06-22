#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 10:25:34 2017

@author: mulang
"""

import cPickle as pickle
import re
import os, sys
from practnlptools.tools import Annotator
import csv

proj_dir = os.path.abspath(os.path.join('..'))
binaries_dir = os.path.abspath(os.path.join('..','DBPedia','onto_binaries'))
sys.path.append(proj_dir)
dbpedia_prop = os.path.abspath(os.path.join(binaries_dir,"prop"))
rels_file = os.path.abspath(os.path.join('..','DBPedia','rel_words.txt'))


from utils import strings
from utils import wordnetProc


annotator=Annotator()
annotations = annotator.getAnnotations("currency code",dep_parse=True)

#HERE CREATE A CLASS OF PREDICATE : TO REP A PREDICATE AND ALL IT'S ATTRIBUTES

class KBproperty(object):
    def __init__(self):
        self.prop_uri = ""
        self.domain = ""
        self.range = ""
        self.label = ""
        self.comment = ""
        self.instances_count = 0
        self.uniq_subjs = 0
        self.uniq_objs = 0
        self.annotations = None
        self.phrases =  None
        self.syn_hypo = None
            
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
        dep_seq.append(positions)    
    return (bag_of_words,pos_seq,ner_seq,chunk_seq,dep_seq,srls)


#PROCESSS THE FILES
def file_processor() :
    pred_file = os.path.join(proj_dir,"DBPedia","onto_counts_ratio")
    
    
    words_dict = {}
    
    with open(rels_file) as f:
        words = f.readlines()
        
        for line in words:
            #print line
            entries = line.split(":")
            words_dict[entries[0].strip(" ")] = entries[1].split(",")
    
    #ORDER OF THE ITEMS : "property","domain","range","label","comment",count
    with open(pred_file) as f:
        predicates = csv.reader(f)
        i = 0
        for row in predicates:
            kb_prop = KBproperty()
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
            
            if pred_label.lower() == "population total" :
               
                kb_prop.label = pred_label
                
                count = row[-3]
                unq_sbj_count = row[-2]
                unq_obj_count = row[-1]
                                        
                kb_prop.instances_count = int(count)
                kb_prop.uniq_subjs = unq_sbj_count
                kb_prop.uniq_subjs = unq_obj_count
                
                #HERE WE SHIFT THE LABESLS THAT ARE REALY JUST COMMENTS AND GENERATE NEW LABELS
                if (len(row[0].split("/")[-1]) < (len(pred_label) - len(pred_label.split(' '))) and pred_label.find("(")==-1) :
                    row[4] = pred_label
                    row[3] = row[0].split("/")[-1]
                    pred_label = strings.split_string_on_caps(row[3].replace("'",""))        
                
                comment =row[4].replace('(','').replace(')','').strip()
                comment =  re.sub(r"^'|'$", "", comment)
                comment =  re.sub(r'^"|"$', '', comment)
                            
                kb_prop.comment = comment
                
                synonyms = wordnetProc.get_synonyms(pred_label,'n')           
                hyponyms = wordnetProc.get_hyponyms(pred_label,'n')
                
                if pred_label.lower() in words_dict :
                    kb_prop.phrases = words_dict[pred_label.lower()]          
                    
                kb_prop.syn_hypo = ''.join(w for w in synonyms)
                kb_prop.syn_hypo = kb_prop.syn_hypo.join(w for w in hyponyms)
                                        
                sentence = domain_word.strip(" ")+ " "+pred_label.strip(" ")+ " "+  range_word.strip(" ")
                if len(comment)>0 :
                    sentence = sentence+" "+ comment
                    
                
                print kb_prop.phrases
                
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
                                        
                '''with open(dbpedia_prop+"_"+str(i)+".pkl", "wb") as data_file:
                    pickle.dump(kb_prop, data_file)
                    data_file.close'''
            
            i=i+1
               
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

def main():
    file_processor()
    
if __name__== "__main__":
  main()