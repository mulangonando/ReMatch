#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 12:27:45 2017

@author: mulang
"""

from nltk.tag.stanford import StanfordNERTagger
from practnlptools.tools import Annotator

#Classes

class Annotations(object):
    def __init__(self, sentence, dep_req = True):
        self.sentence = sentence
        self.bag_of_words = []
        self.srl = []
        self.poss = []
        self.ners = []
        self.chunks = []
        self.dep_pasre = []
        
    def extract_annotations(self, annotations):
        self.srls = annotations['srl']
        self.poss = annotations['pos']
        self.ners = annotations['ner']
        self.chunks = annotations['chunk']
        
        if self.dep_req :
            self.dep_parse = annotations['dep_parse']
            
        bag_of_words = []
        pos_seq = []
        ner_seq = []
        chunk_seq = []
        dep_seq = []
        for pos in self.poss :
            bag_of_words.append(pos[0])
            pos_seq.append(pos[1])
        
        for ner in ners :
            ner_seq.append(ner[1])
        
        for chunk in chunks :
            chunk_seq.append(chunk[1])
        
        dep_seq = []
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
    
    
    print sentence, "\n\n"
            annotator=Annotator()
            prop_ann = annotator.getAnnotations(sentence,dep_parse=True)
                        
            kb_prop.annotations = extract_annotations(prop_ann)            
            KBproperty.all_props.append(kb_prop)
            
            #print bag_of_words,pos_seq,ner_seq,chunk_seq,dep_seq,srls, "\n"