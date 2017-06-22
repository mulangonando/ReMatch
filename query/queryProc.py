#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 21:59:14 2017

@author: mulang
"""

from nltk.tag.stanford import StanfordNERTagger
from practnlptools.tools import Annotator
from nltk.stem import WordNetLemmatizer 
from utils import wordnetProc
from QuestionClassification import single_coarse_class 
import csv
import os

gazzet_file = os.path.abspath(os.path.join('.','Gazetteer','countries.csv'))
countries_list = []

with open(gazzet_file) as c:
    countries = csv.reader(c)
   
    for row in countries:
        countries_list.append(row[0].lower())
        countries_list.append(row[1].lower())
        countries_list.append(row[2].lower())
        countries_list.append(row[3].lower())
        
#Classes
class Relation(object):
    def __init__(self, desire,head,head_pos,prep,left,helper,helper_pos,right,num_nps,named_entities,non_ent_nouns ):
        self.desire = desire
        self.head = head
        self.head_pos = head_pos
        self.prep = prep
        self.left = left
        self.helper = helper
        self.helper_pos=helper_pos
        self.right = right
        self.num_nps = num_nps
        self.named_entities = named_entities
        self.non_ent_nouns = non_ent_nouns
        
    def __del__(self):
        self.close()
        
 

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

def extract_entity_classes(ner_seq):
    nouns = []
    for ne in ner_seq :
        if ne != "O":
            if ne[ne.find("-")+1:] == "PER" and "person" not in nouns :
                nouns.append("person")
            elif ne[ne.find("-")+1:] == "ORG" and "organization" not in nouns :
                nouns.append("organization")
            elif ne[ne.find("-")+1:] == "LOC" and "location" not in nouns :
                nouns.append("location")
    return nouns

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
        
def extract_non_entity_nouns(bag_of_words,pos_seq,ner_seq):
    non_ent_nouns = []
    
    i = 0
    for pos in pos_seq :
        if pos.find('NN')>-1 and ner_seq[i]=='O':
            non_ent_nouns.append(bag_of_words[i])
        i=i+1
        
    return non_ent_nouns  

def num_noun_phrases(chunk_seq,pos_seq):
    count_nps = 0
    i=0
    for chunk in chunk_seq :
        if chunk.find("B-NP")>-1 or (chunk.find("S-NP")>-1 and pos_seq[i] != 'PRP') :
            count_nps = count_nps +1
    i=i+1
            
    return count_nps

def extract_named_entities(bag_of_words, ner_seq):
    neents = []
    i=0
    for ner in ner_seq :
        if ner != 'O':
            neents.append(bag_of_words[i])
        i=i+1
    return neents

'''def label_characteristics(num_nes,bag_of_words,pos_seq,ner_seq,chunk_seq,dep_seq):
    root=int(extract_root(dep_seq))
    verbs = extract_verb_positions(pos_seq)
    qw_pos = pos_seq[0]
    type_chunk_after = ""
    if root<len(bag_of_words) :
        type_chunk_after = chunk_seq[root]
    type_chuck_bef = chunk_seq[root-2]
    type_head_word = pos_seq[root-1]
    qw = 'none'    
    quantifier = "none"
    imed_preposition = "none"
    nes_label ="none"
    verb_att_type = [] #Dependency of the verb with the root word
    
    label_attribs = {}
    
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
            
    if root<len(bag_of_words) and (pos_seq[root] == "IN" or bag_of_words[root] == "TO"):
        imed_preposition =  [root]
    elif  pos_seq[root-2] == "IN":        
        imed_preposition =  bag_of_words[root-2]
    
    #for chunk in chunk_seq :
    #    if 
    #We want ti check the type of head word, if Verb, then let's find it's clossed related noun
    
    label_attribs["verbs"] = verbs
    label_attribs["qw_pos"]=qw_pos
    label_attribs["type_chunk_after"] = type_chunk_after
    label_attribs["type_chuck_bef"] = type_chuck_bef
    label_attribs["type_head_word"] = type_head_word
    label_attribs["qw"] = qw
    label_attribs["quantifier"] = quantifier
    label_attribs["imed_preposition"] = imed_preposition
    label_attribs["nes_label"] = nes_label
    label_attribs["verb_att_type"] = verb_att_type 
        
    return label_attribs
    

def count_characteristics (bag_of_words,pos_seq,ner_seq,chunk_seq,dep_seq) :
    #WE can gwt the qw = '' from the Bag of words
    count_attribs = {}
    root = int(extract_root(dep_seq))
    count_attribs["root"] = root
        
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
    dist_ne_normalize = 0 #Magnitude of the distabce divided by the number of the position of the root word
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

    
    count_attribs["rel_head_qw"] = rel_head_qw
    count_attribs["verbs"] = verbs
    count_attribs["num_nps"] = num_nps
    count_attribs["num_nes"] = num_nes
    count_attribs["qw_independence"] = qw_independence
    count_attribs["dist_ne_normalize"] = dist_ne_normalize
    count_attribs["verb_helper"] = verb_helper
    count_attribs["verb_main"] = verb_main
    count_attribs["nearest_np_after"] = nearest_np_after
    count_attribs["named_entits_rel"] = named_entits_rel
    count_attribs["subj"] = subj
    count_attribs["other_verb_subj"] = other_verb_subj
    count_attribs["obj"] = obj
    count_attribs["other_verb"] = other_verb
    count_attribs["other_verb_obj"] = other_verb_obj
         
    return count_attribs  '''

def get_helper_words(dep_seq,pos_seq,bag_of_words,index):
    obj_subj = -1
    helper = -1
    non_obsub_support = ["dobj","iobj","nsubjpass","nsubj","csubj"] #dependencies that should not be in the dep to support a noun
    non_help_support = ['WDT', 'IN', 'TO', '.']  #POS that cant help the relations
    
    for dep in dep_seq :
        if(int(dep[1]) == (index+1) and str(dep[0]) != "det" and int(dep[2]) < (index+1)):
            if(str(dep[0]) in non_obsub_support) :
                obj_subj = int(dep[2]) - 1
                #return int(dep[2]) - 1
            elif pos_seq[int(dep[2]) - 1] not in non_help_support :
                helper = int(dep[2]) - 1
            
        elif(int(dep[2]) == (index+1) and int(dep[1]) < (index+1)) :
            if(str(dep[0]) in non_obsub_support) :
                obj_subj = int(dep[1]) - 1
                #return int(dep[2]) - 1
            elif pos_seq[int(dep[1]) - 1] not in non_help_support :
                helper = int(dep[1]) - 1
    
    return     (obj_subj,helper)      
        
def rel_adjustment (rel,bag_of_words,pos_seq) :
    rels = []
    if rel.head_pos.find("VB")>-1 and rel.head == bag_of_words[0] and rel.num_nps >0 :
        if len(rel.non_ent_nouns) >0 :
            rel.head = rel.non_ent_nouns[-1]
        elif len(rel.named_entities)>0 :
            rel.head = rel.named_entities[-1] 
        rels.append(rel)
    else :
        lemmatizer = WordNetLemmatizer()
        rel_lemma = rel.head
        try:
            rel_lemma = lemmatizer.lemmatize(rel.head,wordnetProc.penn_to_wn(rel.head_pos))
        except:
            pass
        
        if rel_lemma =="have" or rel_lemma =="be" or rel_lemma =="do"  :
           print str(pos_seq[-2]),"   ",str(pos_seq[-2])
           
           if str(pos_seq[-2]).find("VB") >-1 or str(pos_seq[-2]).find("JJ")>-1 :
               rel.head_pos = rel.head_pos+" "+pos_seq[-2]
               rel.head = rel.head+ " "+ bag_of_words[-2] 
               
               rels.append(rel)
           
           elif len(rel.non_ent_nouns)>0 :
               print rel_lemma
               rel.head_pos == "NN"
               i=0
               for noun in rel.non_ent_nouns :
                   if i==0 :
                       rel.head=noun
                       rel.helper = bag_of_words[bag_of_words.index(noun)-1]
                       
                       print bag_of_words[bag_of_words.index(noun)-1]
                       if bag_of_words[0].lower() == "where" :
                           rel.non_ent_nouns.append("place")
                       elif bag_of_words[0].lower() == "when" :
                           rel.non_ent_nouns.append("date")
                       
                       rels.append(rel)
                   else :
                       new_rel = Relation(rel.desire,noun,rel.head_pos,"",rel.left,rel.helper,rel.head_pos,
                                           rel.right,rel.num_nps,rel.named_entities,rel.non_ent_nouns)
                       if bag_of_words[0].lower() == "where" :
                           new_rel.non_ent_nouns.append("place")
                       elif bag_of_words[0].lower() == "when" :
                           new_rel.non_ent_nouns.append("date")
                       
                       rels.append(new_rel)
                   i=i+1
           else :
               #print "GOT Herest",rel.named_entities#, rel.right
               rel.helper = rel.head
               rel.head = rel.named_entities[-1] 
 
               if bag_of_words[0].lower() == "where" :
                   rel.non_ent_nouns.append("place")
               elif bag_of_words[0].lower() == "when" :
                   rel.non_ent_nouns.append("date")
               rels.append(rel)
                 
        else :

            if bag_of_words[0].lower() == "where" :
                rel.non_ent_nouns.append("place")
            elif bag_of_words[0].lower() == "when" :
                rel.non_ent_nouns.append("date")
            rels.append(rel)
        #print rel.non_ent_nouns,rel.named_entities#,rel.left#, rel.right#, rel.helper
        
    return rels
        
def binary_relations (desire,bag_of_words,pos_seq,ner_seq,chunk_seq,dep_seq):
    verb_poss = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
    bin_rels=[]
    question_words = ['who', 'how', 'why', 'whom', 'which', 'when', "where"] 
    non_obj_support = ['WDT', 'IN', 'VBZ', 'VBN', 'TO', '.','WP'] 
    rel_eq_root = False
    root = int(extract_root(dep_seq))
    root_subj_index = -1
    root_obj_index = -1 
    helper_pos =""
    head_pos =""
    rel_eliminator = {}
    #nouns = extract_entity_classes(ner_seq)
    
    root_partmod_index = -1
    
    for dep in dep_seq :
        try:
            #curr_rel=None
            prep = "of"
            rel=None 
            gazz_word = ""
            
            if(str(dep[0])[0:5] == "prep_"):
                
                prep=str(dep[0])[(str(dep[0]).find("_")+1):]
                k=int(dep[2])-1
                j=k-1
                
                obj_chunk = chunk_seq[k]
                obj_phrase = bag_of_words[k]
                
                if ner_seq[k].find("-LOC"):
                    if bag_of_words[k].lower() in countries_list:
                        gazz_word = "country"
                
                while obj_chunk != "S-NP" and obj_chunk != "E-NP":
                    obj_chunk = chunk_seq[k+1]
                    obj_phrase = obj_phrase +" "+bag_of_words[k+1]
                    k = k+1
                    
                if k==int(dep[2])-1 :
                    obj_chunk = chunk_seq[j] 
                    while obj_chunk != "S-NP" and obj_chunk.find("-NP") !=-1 and (pos_seq[j] not in non_obj_support) and j>0:
                            obj_phrase = bag_of_words[j]+" " + obj_phrase
                            obj_chunk = chunk_seq[j]                                       
                            j = j-1
                         
                rel = bag_of_words[int(dep[1])-1]
                head_pos = pos_seq[int(dep[1])-1]
                
                #THIS IF STATEMENT TAKES CARRE OF PHRSES SUCH AS vice president of .... ETC
                if chunk_seq[int(dep[1])-1].find("NP")>-1 and chunk_seq[int(dep[1])-2].find("NP")>-1 and pos_seq[int(dep[1])-2].find("NN")>-1 : 
                    rel = bag_of_words[int(dep[1])-2]+" "+rel
                    head_pos = "NNP"
                
                if root == int(dep[1]) :
                    rel_eq_root = True
                    #print "Relation: " , rel                 
            
            elif int(dep[1]) == root and str(dep[0])[0:5] == "nsubj" :
                #print "GOT HERE"
                root_subj_index = int(dep[2])-1
                
            elif int(dep[1]) == root and str(dep[0])[0:4] == "dobj" :
                #print "GOT HERE"
                root_obj_index = int(dep[2])-1
                
            elif str(dep[2]) == str(root) and str(dep[0])[0:5] == "nsubj" :
                #print "GOT HERE"
                root_subj_index = int(dep[1])-1
                
            elif str(dep[2]) == str(root) and str(dep[0])[0:4] == "dobj" :
                root_obj_index = int(dep[1])-1
                  
            elif str(dep[0])[0:7] == "partmod" and int(dep[1])-1==root_subj_index and ner_seq[int(dep[2])-1] == "O":
                root_partmod_index = int(dep[2])-1
                
            if (str(dep[0])[0:] == "dep" or str(dep[0])[0:] =="amod") and int(dep[1]) == root and ner_seq[int(dep[2])-1] == "O" and pos_seq[int(dep[2])-1] not in verb_poss and pos_seq[int(dep[2])-1] not in non_obj_support:
                #print "The dep is :", bag_of_words[int(dep[2])-1], '\n', dep 
                root_partmod_index = int(dep[2])-1
                #print 'Root part mod : ', root_partmod_index
                
            if rel != None :               
                subj_phrase = None
                helper = None
                    
                (obj_subj,helper_word) = get_helper_words(dep_seq,pos_seq,bag_of_words,int(dep[1])-1)  
                    
                if  helper_word > -1 :
                    helper = bag_of_words[int(helper_word)]
                    helper_pos = pos_seq[int(helper_word)]
                    subj_phrase = bag_of_words[int(obj_subj)]
                                    
                    j=int(obj_subj)
                    subj_chunk =chunk_seq[j]
                    
                    #GO LEFT TO THE BEGINING OF THE PHRASE
                    while subj_chunk != "S-NP" and subj_chunk != "B-NP" and j>0:
                        subj_chunk = chunk_seq[j-1]
                        subj_phrase = bag_of_words[j-1]+" "+subj_phrase                                   
                        j = j-1
                    
                #print subj
                
                if subj_phrase == None or subj_phrase.find(obj_phrase)>-1 or (subj_phrase.lower() in question_words):
                    subj_phrase = "?" 
                    
                elif (obj_phrase.lower() in question_words):
                    obj_phrase = "?"
                    
                if helper == None :
                    helper = ""
                    
                non_ent_nouns = extract_non_entity_nouns(bag_of_words,pos_seq,ner_seq)#.append(gazz_word)
                named_entities = extract_named_entities(bag_of_words, ner_seq)
                num_nps = num_noun_phrases (chunk_seq,pos_seq)
                curr_rel=Relation(desire,rel, head_pos,prep,subj_phrase, helper,helper_pos,obj_phrase,num_nps,named_entities,non_ent_nouns)
                
                curr_rels = rel_adjustment (curr_rel,bag_of_words,pos_seq)
                for curr in curr_rels :
                    if len(curr.helper)>0 :
                        rel_eliminator[len(rel_eliminator)] = curr.helper +" "+ curr.head  
                    else:
                        rel_eliminator[len(rel_eliminator)] = curr.head  
                    bin_rels.append(curr)
        except:
            pass
                                           
    i=0        
    for word in bag_of_words :
        curr_rel=[]
        rel = None
        prep ="of"
        if word == "'s" or word == "'":
            
            subj_chunk = chunk_seq[i+1 ]
            #rel = bag_of_words[i+1]
            subject_phrase = bag_of_words[i+1]
            
            k=i+1
            
            while subj_chunk != "S-NP" and subj_chunk != "E-NP":
                subj_chunk = chunk_seq[k+1]
                subject_phrase = subject_phrase +" "+bag_of_words[k+1]
                
                k = k+1
                
            rel = subject_phrase
            head_pos="NP"
            
            object_phrase = bag_of_words[i-1]
            obj_chunk = chunk_seq[i-1 ]
            
            j=i-1
            
            #GO LEFT TO THE BEGINING OF THE PHRASE
            while obj_chunk != "S-NP" and obj_chunk != "B-NP" and j>0:
                obj_chunk = chunk_seq[j-1]
                object_phrase = bag_of_words[j-1]+" "+object_phrase
               
                j = j-1
                        
            if(ner_seq[i-1].find("-LOC") > -1 ) :
                prep = "in"
                helper = "location place"
                
            
            #FOR THIS CASE WE DONT LOOK FOR THE SUBJECT, WE KNOW THE OBJECT AND RELATION         
            if rel != None :
                subj = "?"
                helper = ""
                
                if bag_of_words[root-1] == rel :
                   rel_eq_root = True 
                                                
            non_ent_nouns = extract_non_entity_nouns(bag_of_words,pos_seq,ner_seq)#.append(gazz_word)
            named_entities = extract_named_entities(bag_of_words, ner_seq)
            num_nps = num_noun_phrases (chunk_seq,pos_seq)
            #helper = helper + gazz_word
            curr_rel=Relation(desire,rel,head_pos, prep,subj, helper,helper_pos,object_phrase,num_nps,named_entities,non_ent_nouns)
            
            bin_rels.append(curr_rel)
            if len(curr.helper)>0 :
                rel_eliminator[len(rel_eliminator)] = curr.helper +" "+ curr.head  
            else:
                rel_eliminator[len(rel_eliminator)] = curr.head  
                                   
        i=i+1 
    
       
    # NO POINT HERE JUST CHECK IF ANY OF ALREADY FOUND RELATIONS CONTAIN THE ROOT
    if not rel_eq_root :
        #print "Head POS : ",head_pos 
        root_subj =""
        root_obj = ""
        
        rel_index = -1
        #print 'Relation before . ',rel 
        if root_partmod_index > -1 :
           
            helper = bag_of_words[root-1]
            helper_pos=pos_seq[root-1]
            rel = bag_of_words[root_partmod_index ]
            
            head_pos = pos_seq[root_partmod_index]
            rel_index = root_partmod_index
            
        else :
            #THIS CASE SHOWS THAT THERE ARE NO PREPOSITIONS HENCE THE SENTENCE IS EITHER TOO SHORT OR CONTAINS OTHER ELEMENTS
            rel = bag_of_words[root-1]
            head_pos=pos_seq[root-1]
            rel_index = root-1
            helper = ""
        z=1    
        for dep in dep_seq :
            try:          
                #if int(dep[1]) == rel_index +1 and str(dep[0])=="dobj" and root_obj=="":#use helper index
                if root_obj_index > -1 and int(dep[2])-1 == root_obj_index: 
                                    
                    root_obj = root_obj+bag_of_words[root_obj_index]#root_obj = root_obj+" "+bag_of_words[int(dep[2])-1]
                    
                    root_obj_chunk = chunk_seq[int(dep[2])-1]
                    root_obj_chunk = chunk_seq[root_obj_index]
                     
                    k=int(dep[2])-1 #Forwards counter
                    j=k #Backwards counter
            
                    while root_obj_chunk != "S-NP" and root_obj_chunk != "E-NP" :
                        root_obj_chunk = chunk_seq[k+1]
                        root_obj = root_obj +" "+bag_of_words[k+1]
                        k = k+1
                    
                    if k==int(dep[2])-1 :
                        root_obj_chunk = chunk_seq[j]
                        while root_obj_chunk != "S-NP" and root_obj_chunk != "B-NP" and root_obj_chunk.find("-NP") !=-1 and (pos_seq[j] not in non_obj_support) and j>0:
                            
                            root_obj = bag_of_words[j-1]+" " + root_obj
                            root_obj_chunk = chunk_seq[j-1]                                                                            
                            j = j-1
                        
                #elif int(dep[1]) == rel_index +1 and str(dep[0])=="nsubj" and root_subj=="":
                elif root_subj_index > -1 and int(dep[2])-1 == root_subj_index :
                    root_subj = bag_of_words[int(dep[2])-1]                                
                    root_subj_chunk = chunk_seq[int(dep[2])-1]
                    
                    k=int(dep[2])-1 #Forwards counter
                    j=k #Backwards counter
            
                    while root_subj_chunk != "S-NP" and root_subj_chunk != "E-NP" :
                        root_subj_chunk = chunk_seq[k+1]
                        root_subj = root_subj +" "+bag_of_words[k+1]                        
                        k = k+1
                    
                    if k==int(dep[2])-1 :
                        while root_subj_chunk != "B-NP" and root_subj_chunk != "S-NP" and root_subj_chunk.find("-NP") !=-1 and (pos_seq[j] not in non_obj_support) and j>0:
                            root_subj = bag_of_words[j-1]+" " + root_subj
                            root_subj_chunk = chunk_seq[j-1]                                          
                            j = j-1
                z = z +1
            except:
                pass
            
               
        if  len(root_subj) < 1:
            root_subj ="?"
            
        if  len(root_obj) < 1: 
            root_obj = "?"
        prep = ""    
        
        #TAKE CARE OF ALL nn RELATIONS THAT ARE IN NAMED ENTITIES IN CHUNKS BUT NOT IN THE OBJECTS OR SUBJECTS 
        non_ent_nouns = extract_non_entity_nouns(bag_of_words,pos_seq,ner_seq)#.append(gazz_word)
        named_entities = extract_named_entities(bag_of_words, ner_seq)
        num_nps = num_noun_phrases (chunk_seq,pos_seq)
        curr_rel=Relation(desire,rel,head_pos, prep,root_subj, helper,helper_pos,root_obj, num_nps,named_entities,non_ent_nouns)
        curr_rels = rel_adjustment (curr_rel,bag_of_words,pos_seq)
        for curr in curr_rels :
            if len(curr.helper)>0 :
                rel_eliminator[len(rel_eliminator)] = curr.helper +" "+ curr.head  
            else:
                rel_eliminator[len(rel_eliminator)] = curr.head
                
            bin_rels.append(curr)
    i = 0
    
    for rel in bin_rels :
        
        for j in range(len(rel_eliminator)) :
            
            if i == j :
                pass
            
            else :                        
                if (rel.helper == bin_rels[j].helper or rel.head == bin_rels[j].helper) :
                    if (rel.head_pos=='VBP' and bin_rels[j].head_pos=='JJ') :
                        rel.head = bin_rels[j].head +" "+ rel.head 
                        #rel.helper = rel.helper +" "+ bin_rels[j].helper                                            
                                
                    if (rel.head_pos=='JJ' and bin_rels[j].head_pos=='VBP') :
                        rel.head = rel.head +" "+ bin_rels[j].head                
                
                #print "ELIMINATOR :", rel_eliminator
                rel_tokens = rel_eliminator.get(j).split(" ")
                              
                #print "Current Tokens : ",rel_tokens
                for token in rel_tokens :
                   #print "The Token : ",token,"\n The LIST : ", rel.non_ent_nouns
                   try:
                       rel.non_ent_nouns.remove(token)
                   except :
                       pass
                   
        for n in rel.named_entities:
                if n.lower() in countries_list and rel.prep=="of":
                    rel.helper = rel.helper + " " +"country"
                    
        for n in rel.non_ent_nouns :
                if n.lower() in countries_list and rel.prep=="of" :
                    rel.helper = rel.helper + " " +"country"
        
        for n in rel.left :
                if n.lower() in countries_list and rel.prep=="of" :
                    rel.helper = rel.helper + " " +"country"
        
        for n in rel.right :
                if n.lower() in countries_list  and rel.prep =="of" :
                    rel.helper = rel.helper + " " +"country"
                        
    return bin_rels

def recursive_binaries(bag_of_words,pos_seq,ner_seq,chunk_seq,dep_seq,pos,binaries=[], sent_words = []):
    adj_clause_words=["who","whom","whose","which","that"]
    if pos==0:        
        return binaries
    else:
        sentence = ""
        
        for i in range(pos, 0, -1):
            if bag_of_words[i].lower() in adj_clause_words and i>1 :
                j = i-1
                noun_chunk = chunk_seq[j-1] 
                noun = bag_of_words[j]
                #print noun
                
                while j-1>-1 and noun_chunk != "S-NP" and noun_chunk.find("-NP") !=-1 :
                    j = j-1
                    noun = bag_of_words[j]+" " +noun
                    noun_chunk = chunk_seq[j-1]                                                
                    
                sentence = noun +" "+ sentence #bag_of_words[0]+" "+noun +" "+ sentence

                sent_annotator=Annotator()
                
                sent_annotations = sent_annotator.getAnnotations(sentence,dep_parse=True)
                (sent_words,sent_pos_seq,sent_ner_seq,sent_chunk_seq,sent_dep_seq,sent_srls) = extract_annotations(sent_annotations)
                #(sent_words,sent_pos_seq,sent_ner_seq,sent_chunk_seq,sent_dep_seq,sent_srls)
                
                desire = single_coarse_class.question_desire(sentence)
                bin_rels = binary_relations(desire,sent_words,sent_pos_seq,sent_ner_seq,sent_chunk_seq,sent_dep_seq)

                for rel in bin_rels:
                    binaries.append(rel)
                    
                #ALSO PROCESS THE LEFT SIDE
                left_sentence = ""
                for j in range(0,i):
                    left_sentence = left_sentence + " "+bag_of_words[j]
                
                left_annotations = sent_annotator.getAnnotations(left_sentence,dep_parse=True)
                (left_words,left_pos_seq,left_ner_seq,left_chunk_seq,left_dep_seq,left_srls) = extract_annotations(left_annotations)
                return recursive_binaries(left_words,left_pos_seq,left_ner_seq,left_chunk_seq,left_dep_seq,len(left_words)-1,binaries, sent_words)
                
            else :        
                sentence = bag_of_words[i] +" "+ sentence
        
        #print "THe Sentence : ", sentence        
        sentence = bag_of_words[0] + sentence        
        desire = single_coarse_class.question_desire(sentence)
        bin_rels = binary_relations(desire,bag_of_words,pos_seq,ner_seq,chunk_seq,dep_seq)
        
    
        for rel in bin_rels:
        
            binaries.append(rel)
        
        return binaries #recursive_binaries(bag_of_words[:i],pos_seq[:i],ner_seq[:i],chunk_seq[:i],dep_seq[:i],0,binaries, sent_words)          
        
