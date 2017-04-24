#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 16:12:45 2017

@author: mulang
"""

from nltk.corpus import wordnet as wn
from nltk.corpus.reader.wordnet import WordNetError
from nltk.stem import WordNetLemmatizer
from nltk.stem import SnowballStemmer
import numpy as np

import editdistance

def dist_all_synsets(first,second) : 
    f_syns = wn.synsets(first)
    #print f_syns, "\n\n"
    
    s_syns = wn.synsets(second)
    #print s_syns, "\n\n"
    
    #Path SImilarity
    #A 0-1 similarity score based on the shortest path that connects the senses in the is-a (hypernym/hypnoym) taxonomy.
    #A score of 1 represents identity i.e. comparing a sense with itself will return 1.
    least_sim = 0.0
    for f in f_syns :
        
        for s in s_syns :
            path_sim = wn.path_similarity(f,s)
            #print path_sim
            #print least_sim
            if path_sim > least_sim :
                #print path_sim
                #print least_sim
                least_sim = path_sim;
    
    #Leacock-Chodorow Similarity
    #A similarity score of the shortest path connecting the senses & the maximum depth of the taxonomy in which the senses occur. 
    #The relationship is given as -log(p/2d) where p is the shortest path length and d the taxonomy depth.
    
    max_lch=0.0
    for f in f_syns :
        
        for s in s_syns :
            lch = 0.0
            try :
                lch = wn.lch_similarity(s,f)
            except WordNetError :
                pass
            
            #if ".n." in str(s) and ".n." in str(f) :
            #    lch = wn.lch_similarity(s,f)
            #    print lch
            #elif ".v." in str(s) and ".v." in str(f) :
            #    lch = wn.lch_similarity(s,f)
            #    print lch
            #elif ".a." in str(s) and ".a." in str(f) :
            #    lch = wn.lch_similarity(s,f)
                            
            if lch > max_lch :
                max_lch = lch;
    
    #Wu-Palmer Similarity
    #A similarity score based on the depth of the two senses in the taxonomy and that of their Least Common Subsumer (most specific ancestor node).
    #The LCS does not necessarily feature in the shortest path connecting the two senses, as it is by definition the common ancestor deepest in the taxonomy, not closest to the two senses. Typically, however, it will so feature. Where multiple candidates for the LCS exist, that whose shortest path to the root node is the longest will be selected. Where the LCS has multiple paths to the root, the longer path is used for the purposes of the calculation.

    wup_sim = wn.wup_similarity(f_syns[0],s_syns[0])
    
    if(wup_sim == None) :
            wup_sim=-1
    
    #print path_sim,lch_sim, wup_sim 
    
    return (least_sim,max_lch,wup_sim )

def derivational_forms(first, second):
    #Checks if there are any derivationally related forms of the word lemmas that match
    f_syns = wn.synsets(first)
    s_syns = wn.synsets(second)
    #print s_syns
    
    for i in f_syns :
        sub_i = str(i)[8:-2]
        curr_lemma = wn.lemma(sub_i+"."+sub_i[0:sub_i.index(".")])
        derived_forms = curr_lemma.derivationally_related_forms()
        
        
        for derived in derived_forms :
            
             rep1 = str(derived)[7:str(derived).index(".")]
             index = str(derived).index(rep1)+len(rep1)+6
             rep2 = str(derived)[index:-2]
             
             if rep1 == second:
                     return 1
             elif rep1 != rep2 :
                 if rep2 == second:
                     return 1
                 
             for s in s_syns : 
                 s_str = str(s)[8:str(s).index(".")]
                 sub_s = str(s)[8:-2]
                 
                 if rep1 == s_str:
                     return 0.75
                 elif rep1 != rep2 :
                    if rep2 == s_str:
                        return 0.75
                    
                 s_curr_lemma = wn.lemma(sub_s+"."+s_str )
                 s_derived_forms = s_curr_lemma.derivationally_related_forms()
                 
                 for match in s_derived_forms :
                     
                     match_rep1 = str(derived)[7:str(derived).index(".")]
                     match_index = str(derived).index(rep1)+len(rep1)+6
                     match_rep2 = str(derived)[match_index:-2]
                     
                     if match_rep1 == first:
                         return 1
                     elif match_rep1 != match_rep2 :
                         if match_rep2 == first:
                             return 1
                     
                     if match in derived_forms or match_rep1 == rep1 or match_rep1 == rep2 :
                         return 0.5
                     
    return 0
   

def lev_similarity(first,second):
    lemmatizer = WordNetLemmatizer()
    full_len_diff = abs(len(first)-len(second))
    denom = max(len(first),len(second))
    
    f_lemma = lemmatizer.lemmatize(first)
    s_lemma = lemmatizer.lemmatize(second)
    dist_lemmas = editdistance.eval(f_lemma,s_lemma)
    
    simm_weight = float(denom - dist_lemmas)/denom#1 - (float(dist_lemmas)/float(denom)+ float(dist_stems)/float(denom))/2
    
    return simm_weight

def size_intersection(a,b):
    c = sorted(set(a).intersection(b))
    return len(c)
    
def domain_range_measure(q_type, p_domain, p_range):
    
    return 0
    
def top_similar(all_props, q_rels,count_attribs, label_attribs, q_bag):
    weight1 = 0
    weight2 = 0
    weight3 = 0
    uri = ["","",""]
    for prop in all_props :
        if(q_rels.head.strip().lower() ==  prop.label.strip().lower()) :
            weight1 = 10
            uri[0] = prop.prop_uri
        else :
            rel_words = q_rels.head.split(" ")
            print rel_words, q_rels.helper
            #prop_words = prop.label.split(" ")
            sim_vector = []
            
            #lev_dist = lev_similarity(q_rels.head.strip().lower(), prop.label.strip().lower())
            
            #if len(prop_words)>1 and len(rel_words)>1 and lev_dist >0.8 :
            #  weight1 = 10 
            
            if len(rel_words)>1 :
                spec_word_weight = 0
                for word in rel_words :
                    this_weight = lev_similarity(word,prop.label)
                    if prop.label.strip().lower() == word.strip().lower() :
                        this_weight = this_weight * 5
                                       
                    if this_weight>spec_word_weight :
                        spec_word_weight = this_weight
                
                sim_vector.append(spec_word_weight)
                
            
            
            sim_vector.append(lev_similarity(q_rels.head,prop.label))
            
            try :
                sim_vector.append(derivational_forms(q_rels.head, prop.label))
                (least_sim,max_lch,wup_sim ) = dist_all_synsets(q_rels.head,prop.label)
                sim_vector.append(least_sim)
                sim_vector.append(max_lch)
                sim_vector.append(wup_sim)
            
            except :
                pass
            #print sim_vector
            this_weight = np.sum(sim_vector)
            if this_weight > weight1 :
                weight3 = weight2
                weight2 = weight1
                weight1 = this_weight
                uri[2] = uri[1]
                uri[1]=uri[0]
                uri[0]=prop.prop_uri
    return weight1,weight2,weight3, uri
        
    
#print derivational_forms('spouse','wife')
#print dist_all_synsets('wife','n','spouse','n')
#print lev_similarity('discovery','n','discovered','n')

     