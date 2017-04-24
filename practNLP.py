#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 21:59:14 2017

@author: mulang
"""
from practnlptools.tools import Annotator
from nltk.tag.stanford import StanfordNERTagger

def compute_NER(corpus):
    NER = []
    # fi=open("NER_features_train.txt","w")
    st = StanfordNERTagger('stanford-ner-2014-06-16/classifiers/english.all.3class.distsim.crf.ser.gz',
                   'stanford-ner-2014-06-16/stanford-ner.jar')
    ner = st.tag(corpus.split())
    ner_tag = ""
    for n in ner:
        ner_tag = ner_tag + n[1] + " "
    NER.append(ner_tag)
    return NER

def numbers_to_strings(argument):
    switcher = {
        0: "",
        1: "",
        2: "",
    }
    return switcher.get(argument, "nothing")

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
    
    dep_seq = []
    for dep in dep_parse.split('\n') :
        positions = []
        dep_rel = dep[:dep.index('(')]
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

def extract_root(dep_seq):
    root=0
      
    for dep in dep_seq :
        if(dep[0]=='root') :
            root=dep[2]
    return root

def extract_verb_positions(pos_seq) :
    verbs = []
    i=1
    for pos in pos_seq :
        if pos.find("VB") != -1 :
            verbs.append(i)
        i=i+1
    
    return verbs    
        
    

def label_characteristics(num_nes,bag_of_words,pos_seq,ner_seq,chunk_seq,dep_seq):
    root=int(extract_root(dep_seq))
    verbs = extract_verb_positions(pos_seq)
    qw_pos = pos_seq[0]
    type_chunk_after = chunk_seq[root]
    type_chuck_bef = chunk_seq[root-2]
    type_head_word = pos_seq[root-1]
    qw = 'none'    
    quantifier = "none"
    imed_preposition = "none"
    nes_label ="none"
    verb_att_type = [] #Dependency of the verb with the root word
    
    i=0
    for word in bag_of_words :
        if (word.lower() == "what") or (word.lower() == "when") or (word.lower() == "where") or (word.lower() == "which") or (word.lower() == "why") or (word.lower() == "who") or (word.lower() == "whose") or (word.lower() == "how") :
            qw = word
        elif i>0 : 
            if (bag_of_words[i].lower() == "much" and bag_of_words[i-1].lower() == "how") or (bag_of_words[i].lower() == "many" and bag_of_words[i-1].lower() == "how") :
                quantifier = word
            
        i = i+1
            
    #Now we obtain the verbs that are related to the head word from the dependencies
    for dep in dep_seq :
        #print '\n',dep[2],'\t',dep[1],'\t',root,'\t','\n NER SEQ : ',ner_seq[int(dep[1])-1],'\t',ner_seq[int(dep[2])-1]
        if (int(dep[1])==root) and (int(dep[2]) in verbs):
            verb_att_type.append(dep[0])
        elif (int(dep[2])==root) and (int(dep[1]) in verbs):
            verb_att_type.append(dep[0])
        if (int(dep[2])==root) and (ner_seq[int(dep[1])-1].lower() != "o"):
            nes_label = ner_seq[int(dep[1])-1][2:]
        elif (int(dep[1])==root) and (ner_seq[int(dep[2])-1].lower() != "o"):
            nes_label = ner_seq[int(dep[2])-1][2:]
            
    if pos_seq[root] == "IN" or bag_of_words[root] == "TO":
        imed_preposition =  [root]
    elif  pos_seq[root-2] == "IN":        
        imed_preposition =  bag_of_words[root-2]
    
    #for chunk in chunk_seq :
    #    if 
    
    
    #We want ti check the type of head word, if Verb, then let's find it's clossed related noun
        
    return (verbs, qw_pos, type_chunk_after, type_chuck_bef, type_head_word, qw, quantifier, imed_preposition, nes_label, verb_att_type)
    

def count_characteristics (bag_of_words,pos_seq,ner_seq,chunk_seq,dep_seq) :
    #WE can gwt the qw = '' from the Bag of words
    root = int(extract_root(dep_seq))
    verbs = extract_verb_positions(pos_seq)
    
    rel_head_qw=[] 
    named_entits_rel=0
    subj = -1
    #subjExtr = -1
    obj = -1
    num_nps = 0 
    num_nes = 0
    qw_independence = 0 #Could be from 0 to 4 NP,VP,ADVP,ADJP [1-4], 0 else independent
    num_prep_phrase = 0
    nearest_np_after = -1
    nearest_np_attached = -1
    dist_ne_normalize = 0 #Magnitude of the distabce divided by the number od the position of the root word
    verb_helper = 0
    verb_main = 0
    other_verb  = -1
    other_verb_subj = -1
    other_verb_obj = -1
    
    #print '\n\n',verbs ,'\n\n'
    for dep in dep_seq :
        if(int(dep[2])==1) and (int(dep[1])==root) :
            rel_head_qw.append(dep[0])
        elif(int(dep[1])==1) and (int(dep[2])==root) :
            rel_head_qw.append(dep[0])
        if (int(dep[1])==root) and (int(dep[2]) in verbs) and root<int(dep[2]):
            verb_main=1
        elif (int(dep[2])==root) and (int(dep[1]) in verbs) and root>int(dep[2]):
            verb_helper=1
        elif ner_seq[int(dep[2])-1].lower() != "o" :
            named_entits_rel = 1
            
        for verb in verbs :
            if str(verb) in dep and dep[0]=="nsubj" and verb==root :
                subj = int(dep[2])
            elif str(verb) in dep and dep[0]=="nsubj":
                other_verb_subj = int(dep[2])
                other_verb = verb
            elif str(verb) in dep and dep[0]=="dobj" and verb==root :
                obj = int(dep[2])
            elif str(verb) in dep and dep[0]=="dobj" :
                other_verb_obj = int(dep[2])
                other_verb = verb  
            #elif str(root) in dep and dep[2]
        
    i=0
    for chunk in chunk_seq :
        if i==0:
            if chunk[0]=='B' and chunk[2:]=='NP':
                qw_independence = 1
            elif chunk[0]=='B' and chunk[2:]=='VP':
                qw_independence = 2
            elif chunk[0]=='B' and chunk[2:]=='ADVP':
                qw_independence = 3
            elif chunk[0]=='B' and chunk[2:]=='ADJP':
                qw_independence = 4
                        
        if(chunk=='B-NP' or chunk=='S-NP') :
            num_nps = num_nps + 1
            
        if chunk.find("PP") :
            num_prep_phrase = num_prep_phrase + 1
        
        found = False
        if chunk[2:]=="NP" :
            for dep in dep_seq :
                if str(i+1) in dep and str(root) in dep and found == False :
                    nearest_np_attached = i+1
                    found = True
                elif  str(i+1) in dep and str(root) in dep and found == True and nearest_np_attached>(i+1) :
                    nearest_np_attached = i+1                   
        
        i=i+1
            
    for ner in ner_seq :
        if(ner.lower() != 'o') :
            num_nes = num_nes + 1
        
    
    #Nearest Noun Phrase
    for i in range(int(root),len(chunk_seq)-1):
        if chunk_seq[i].find("NP"):
            nearest_np_after=i+1
            break
    
    
    dist_ne_normalize = nearest_np_after - root #CHECK AGAIN AFTER SOME TIME
             
    return (root,rel_head_qw, num_nps, num_nes, qw_independence, dist_ne_normalize,verb_helper, verb_main, nearest_np_after,named_entits_rel,subj,other_verb_subj,obj,other_verb_obj,other_verb)  
    
        #if(dep[0]=='root') and pos_seq[dep[2]].find('VB') :
        #    root=dep[2]
        #elif (dep[0]=='root')
        
annotator=Annotator()
annotations = annotator.getAnnotations("Alps main part ",dep_parse=True)

(bag_of_words,pos_seq,ner_seq,chunk_seq,dep_seq,srls) = extract_annotations(annotations)

print bag_of_words,"\n",pos_seq,"\n",ner_seq,"\n",chunk_seq,"\n",dep_seq,"\n",srls
print '\n'

(root,rel_head_qw, num_nps, num_nes, qw_independence, dist_ne_normalize,verb_helper, verb_main, nearest_np,named_entits_rel,subj,other_verb_subj,obj,other_verb_obj,other_verb)  = count_characteristics (bag_of_words,pos_seq,ner_seq,chunk_seq,dep_seq)
(verbs, qw_pos, type_chunk_after, type_chuck_bef, type_head_word, qw, quantifier, imed_preposition, nes_label, verb_att_type) = label_characteristics(num_nes,bag_of_words,pos_seq,ner_seq,chunk_seq,dep_seq)

print (root,rel_head_qw, num_nps, num_nes, qw_independence, dist_ne_normalize,verb_helper, verb_main, nearest_np,named_entits_rel,subj,other_verb_subj,obj,other_verb_obj,other_verb)
print '\n'


print (verbs, qw_pos, type_chunk_after, type_chuck_bef, type_head_word, qw,quantifier, imed_preposition, nes_label, verb_att_type)
print '\n'

#type of question word
#Distance of Noun phrase from the head
#Type of hed word (Nown or Verb)
