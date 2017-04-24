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

def process_query(query):
    annotator=Annotator()
    annotations = annotator.getAnnotations(query,dep_parse=True)
    (bag_of_words,pos_seq,ner_seq,chunk_seq,dep_seq,srls) = queryProc.extract_annotations(annotations)
    #print pos_seq,"\n",bag_of_words,"\n",chunk_seq,"\n",dep_seq
    last_pos = len(bag_of_words) - 1    
    
    count_attribs  = queryProc.count_characteristics (bag_of_words,pos_seq,ner_seq,chunk_seq,dep_seq)
    label_attribs= queryProc.label_characteristics(count_attribs["num_nes"],bag_of_words,pos_seq,ner_seq,chunk_seq,dep_seq)
        
    bin_rels = queryProc.recursive_binaries(bag_of_words,pos_seq,ner_seq,chunk_seq,dep_seq,last_pos)
    
    '''prev_rel = ""
    for rel in bin_rels :
        #if rel.head == prev_rel :
            
        print rel.helper,rel.head,rel.prep,"(",rel.left,",",rel.right,")"'''
    return count_attribs, label_attribs, bin_rels, bag_of_words

def similarity_vector():
    print ""
     
    
def main():
    #count_attribs, label_attribs, bin_rels, bag_of_words=process_query("which daughter of Donald trump is married to Donald Hayess ?")
    #count_attribs, label_attribs, bin_rels, bag_of_words=process_query("What is the native city of Hollywood's highest paid actress ?")
    #count_attribs, label_attribs, bin_rels, bag_of_words=process_query("Who was vice president under the president")# who approved the use of atomic weapons against Japan during World War II?")
    #count_attribs, label_attribs, bin_rels, bag_of_words = process_query("How many Golden Globe awards did the daughter of Henry Fonda win?")
    #process_query("Which recipients of the Victoria Cross fought in the Battle of Arnhem?")
    #process_query("Which award did Denzel Washington win in 1998 ?")
    #*process_query("Where is Afghanistan Capital ?")
    #**process_query("How old was Steve Jobs' sister when she first met him?")
    #process_query("Which writers had influenced the philosopher that refused a Nobel Prize?")
    #count_attribs, label_attribs, bin_rels, bag_of_words =process_query("Who is the wife of Barack Obama?")
    #print bag_of_words
    #count_attribs, label_attribs, bin_rels, bag_of_words=process_query("What is the Capital city of Germany")
    #process_query("Who is Obama married to?")
    #annotations = annotator.getAnnotations("Who did Obama give birth to ?",dep_parse=True)
    #count_attribs, label_attribs, bin_rels, bag_of_words=process_query("Which is the capital city of Japan ?")
    #count_attribs, label_attribs, bin_rels, bag_of_words=process_query("Who is the daughter of Barack Obama ?")
    #count_attribs, label_attribs, bin_rels, bag_of_words=process_query("Who is the spouse of Barack Obama ?")
    #count_attribs, label_attribs, bin_rels, bag_of_words=process_query("Who is the wife of Barack Obama ?")
    #count_attribs, label_attribs, bin_rels, bag_of_words=process_query("Which German cities have more than 250000 inhabitants ?")
    #**count_attribs, label_attribs, bin_rels, bag_of_words=process_query("Who was John F. Kennedy's vice president")
    #count_attribs, label_attribs, bin_rels, bag_of_words=process_query("Who is the Mayor of Tel Aviv") leader of - correct
    #count_attribs, label_attribs, bin_rels, bag_of_words=process_query("How many students does the Free University in Amsterdam have?")
    count_attribs, label_attribs, bin_rels, bag_of_words=process_query("What is the second highest mountain on Earth")
    
    all_props = predicates.get_AllKBproperties()
    #bin_rels[0].
    
    print sim.top_similar(all_props, bin_rels[0],count_attribs, label_attribs, bag_of_words)
    print bin_rels[0].head
if __name__== "__main__":
  main()