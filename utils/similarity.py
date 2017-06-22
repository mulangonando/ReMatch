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
from nltk.stem.porter import *
import numpy as np

import editdistance

print_out = "test_file"

def dist_all_synsets(first,second) : 
    
    f_syns = wn.synsets(first)
    s_syns = wn.synsets(second)

    #Path SImilarity
    #A 0-1 similarity score based on the shortest path that connects the senses in the is-a (hypernym/hypnoym) taxonomy.
    #A score of 1 represents identity i.e. comparing a sense with itself will return 1.
    least_sim = 0.0
    try:
        for f in f_syns :
            
            for s in s_syns :
                path_sim = wn.path_similarity(f,s)
                
                if path_sim > least_sim :
                    least_sim = path_sim;
    except :
        pass
    
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
                                
            if lch > max_lch :
                max_lch = lch;
    max_lch = max_lch/3.6375
    #Wu-Palmer Similarity
    #A similarity score based on the depth of the two senses in the taxonomy and that of their Least Common Subsumer (most specific ancestor node).
    #The LCS does not necessarily feature in the shortest path connecting the two senses, as it is by definition the common ancestor deepest in the taxonomy, not closest to the two senses. Typically, however, it will so feature. Where multiple candidates for the LCS exist, that whose shortest path to the root node is the longest will be selected. Where the LCS has multiple paths to the root, the longer path is used for the purposes of the calculation.
    wup_sim = 0
    try :
        
        wup_sim = wn.wup_similarity(f_syns[0],s_syns[0])
        
        if(wup_sim == None) :
                wup_sim=-1
    except :
        pass
    
    return (least_sim,max_lch,wup_sim )

def derivational_forms(first, second):
    #Checks if there are any derivationally related forms of the word lemmas that match
    f_syns = wn.synsets(first)
    s_syns = wn.synsets(second)
    #print s_syns
    try :
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
                         return 1.5
                     elif rep1 != rep2 :
                        if rep2 == s_str:
                            return 1.5
                        
                     s_curr_lemma = wn.lemma(sub_s+"."+s_str )
                     s_derived_forms = s_curr_lemma.derivationally_related_forms()
                     
                     for match in s_derived_forms :
                         
                         match_rep1 = str(derived)[7:str(derived).index(".")]
                         match_index = str(derived).index(rep1)+len(rep1)+6
                         match_rep2 = str(derived)[match_index:-2]
                         
                         if match_rep1 == first:
                             return 2
                         elif match_rep1 != match_rep2 :
                             if match_rep2 == first:
                                 return 2
                         
                         if match in derived_forms or match_rep1 == rep1 or match_rep1 == rep2 :
                             return 1
    except :
        pass
                     
    return 0
   

def lev_similarity(first,second):
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()
    
    denom = max(len(first),len(second))
    
    try:        
        f_lemma = lemmatizer.lemmatize(first)
        s_lemma = lemmatizer.lemmatize(second)
        
        f_stem  = stemmer.stem(first)
        s_stem  = stemmer.stem(second)
        
        stem_denom = max(len(f_stem),len(s_stem))
        
        dist_stems = editdistance.eval(f_stem,s_stem)
        dist_lemmas = editdistance.eval(f_lemma,s_lemma)
    
        simm_weight = float(denom - dist_lemmas)/denom#1 - (float(dist_lemmas)/float(denom)+ float(dist_stems)/float(denom))/2
    
        stem_sim = float(stem_denom - dist_stems)/stem_denom
        
        if abs(len(f_stem)-len(s_stem))<3 and stem_sim>0.7 and (f_stem.find(s_stem)>-1 or s_stem.find(f_stem)>-1) :
            stem_sim = 1
            
            if dist_lemmas > 0.7 :
                dist_lemmas = 1
            
        return simm_weight,stem_sim
    except :
        return 0

def size_intersection(a,b):
    #Remove Stop Words
    
    from nltk.corpus import stopwords
    stop = set(stopwords.words('english'))
    q_bag_no_stop = [i for i in a if i.lower() not in stop]
    prop_bag_no_stop = [i for i in b.split(" ") if i.lower() not in stop]
    
    a_set = set(q_bag_no_stop)
    b_set = set(prop_bag_no_stop)
    
    c = a_set.intersection(b_set)
    len(c)
    
    norm = len(c) /len(q_bag_no_stop)
    return norm
    
def domain_range_measure(q_type, p_domain, p_range):
    if q_type == 'HUM':
        q_type = "person"
    elif q_type == 'NUM':
        q_type = "number"
    elif q_type == 'ENTY':
        q_type = "entity"
    elif q_type == 'DESC':
        q_type = ""
    elif q_type == 'ABBR':
        q_type = "abbreviation"
    elif q_type == 'LOC':
        q_type = "location"
    
    if   q_type == p_domain and q_type == p_range:
        return 1
    elif q_type == p_domain or q_type == p_range:
        return 0.75    
    else:
        f_syns = wn.synsets(q_type)
        s1_syns = wn.synsets(p_domain)
        s2_syns = wn.synsets(p_range)
       
        path_sim_d = 0.0
        path_sim_r = 0.0
        try:
            for f in f_syns :
                
                for s in s1_syns :
                    path_sim1 = wn.path_similarity(f,s)
                    
                    if path_sim1 > path_sim_d :
                        path_sim_d = path_sim1;
                
                for s in s2_syns :
                    path_sim2 = wn.path_similarity(f,s)
                    
                    if path_sim2 > path_sim_r :
                        path_sim_r = path_sim2;
        except :
            pass        
        
        if path_sim_d == path_sim_r and path_sim_d > 0.75:
            return 1
        else :
            return max(path_sim_d,path_sim_r)
    
    return 0

def in_out_degree_measure(instances_count, uniq_subjs, uniq_objs ):
    
    if int(instances_count)==0 or uniq_subjs==0 or uniq_objs==0:
        return 0
    
    else:
        ratio = int(uniq_subjs)/int(uniq_objs)
        
        return (int(instances_count)/15358 * ratio)    
    
    
    
def top_similar(all_props, q_rels, q_bag): 
    weights = [] 
    uri = []
    
    numbers = 1
    for prop in all_props :
        sim_vector = []
        if(q_rels.head.strip().lower() ==  prop.label.strip().lower()) :
            sim_vector.append(20)
           
        else :
            rel_words = q_rels.head.split(" ")
        
            spec_word_weight = 0
            spec_stem_weight = 0
            #if len(rel_words)>1 and len(prop.label)==1:
               
            for word in rel_words:
                for label in prop.label.strip("'").split(" "):
                    this_weight,stem_weight = lev_similarity(word,label)
                    
                    if this_weight <0.85 :
                        this_weight = 0
                    else:
                        this_weight = this_weight * len(label)
                                       
                    if this_weight>spec_word_weight :
                        spec_word_weight = this_weight
                        
                    if stem_weight > 0.95 :
                        stem_weight = stem_weight * len(label)
                    
                    if stem_weight>spec_stem_weight :
                        spec_stem_weight = stem_weight
                   
            sim_vector.append(spec_word_weight) 
            sim_vector.append(spec_stem_weight) 
            
            spec_helper_weight=0
            
            if len(q_rels.helper)>0:
                for label in prop.label.strip("'").split(" "):
                    dist_helper,dist_helper_stem = lev_similarity(q_rels.helper,label) 
                
                    if dist_helper == 1:
                        spec_helper_weight = dist_helper
                
            sim_vector.append(spec_helper_weight)                
            
        #try :
        #print "In try:",q_rels.head
        h_derived_weight=0
        for h in q_rels.head.split(" ") :
            #w = 0
            #for label in prop.label.strip("'").split(" "):
            w =  derivational_forms(h,prop.label)
                
            if w>h_derived_weight:
                h_derived_weight = w
        
        sim_vector.append(h_derived_weight)
        
        #Get the attributes for the head words
        h_least_sim = 0
        h_max_lch = 0
        h_wup_sim = 0
        for h in q_rels.head.split(" ") :
            for label in prop.label.strip("'").split(" "):
                (least_sim,max_lch,wup_sim ) = dist_all_synsets(h,label)
                           
                if least_sim>h_least_sim:
                    h_least_sim = least_sim
                if max_lch>h_max_lch:
                    h_max_lch=max_lch
                if wup_sim>h_wup_sim:
                    h_wup_sim= wup_sim
                
        sim_vector.append(h_least_sim)
        sim_vector.append(h_max_lch)
        sim_vector.append(h_wup_sim)

        hlp_derived_weight=0
        for h in q_rels.helper.split(" ") :
            #for label in prop.label.strip("'").split():                
             w = derivational_forms(h, prop.label)
             if w>hlp_derived_weight:
                 hlp_derived_weight = w
        
        sim_vector.append(hlp_derived_weight)
        
        #Get the attributes for the helper word
        hlp_least_sim = 0
        hlp_max_lch = 0
        hlp_wup_sim = 0
        for h in q_rels.helper.split(" ") :
            #for label in prop.label.strip("'").split(" "):
             (least_sim,max_lch,wup_sim ) = dist_all_synsets(h,prop.label)
               
             if least_sim>hlp_least_sim:
                 hlp_least_sim=least_sim
             if max_lch>h_max_lch:
                 hlp_max_lch=max_lch
             if wup_sim>h_wup_sim:
                 hlp_wup_sim=wup_sim
                
        sim_vector.append(hlp_least_sim)
        sim_vector.append(hlp_max_lch)
        sim_vector.append(hlp_wup_sim)
        
        #Get the attributes for the helper word q_rels.non_ent_nouns :    
        hnn_derived_weight=0
        for h in q_rels.non_ent_nouns:
            #for label in prop.label.strip("'").split(" "):
             w = derivational_forms(h, label)
             if w>hnn_derived_weight:
                 hnn_derived_weight = w
        
        sim_vector.append(hnn_derived_weight)
        
        hnn_least_sim = 0
        hnn_max_lch = 0
        hnn_wup_sim = 0
        for h in q_rels.non_ent_nouns :
            #for label in prop.label.strip("'").split(" "):
            (least_sim,max_lch,wup_sim ) = dist_all_synsets(h,label)
                
            if least_sim>hnn_least_sim:
                 hnn_least_sim=least_sim
            if max_lch>hnn_max_lch:
                 hnn_max_lch=max_lch
            if wup_sim>hnn_wup_sim:
                 hnn_wup_sim=wup_sim
                
        sim_vector.append(hnn_least_sim)
        sim_vector.append(hnn_max_lch)
        sim_vector.append(hnn_wup_sim)
        sim_vector.append(domain_range_measure(q_rels.desire, prop.domain, prop.range))
        sim_vector.append(in_out_degree_measure(prop.instances_count,prop.uniq_subjs,prop.uniq_objs))
        #GETTING THE INTERSECTION OF THE BAG_OF-WORDS
        
        bag_prop = prop.domain+" "+ prop.range+" "+prop.label+ " "+prop.comment
        
        in_sec = size_intersection(q_bag,bag_prop)
        
        sim_vector.append(in_sec)
        #ADDING  THE WEIGHT TO THE RETURN VALUES        
        this_weight = np.sum(sim_vector)            
        size = len(weights)
        
        i=0
        while i<size and i<20 :
            
            if this_weight > weights[i] :
                j=size-2    
                while j>=i:
                    weights[j+1] = weights[j]
                    uri[j+1] = uri[j]
                    j=j-1
                    
                weights[i] = this_weight
                uri[i] = prop.prop_uri  
                
                break
            i = i+1
            
        if i==size and size<20:
            if prop.prop_uri in uri :
                pass
            else :
                weights.append(this_weight)
                uri.append(prop.prop_uri )
                             
                #count_loops = count_loops +1 
        numbers = numbers+1        
       # print "Domain : ",prop.domain,"Range : ",prop.range       
    return weights,uri

     