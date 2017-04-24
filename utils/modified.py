#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 09:56:59 2017

@author: mulang
"""

def top_similar(all_props, q_rels,count_attribs, label_attribs, q_bag):
    weight1 = 0
    weight2 = 0
    weight3 = 0
    uri = ["","",""]
    for prop in all_props :
        if(q_rels.head.strip().lower() ==  prop.label.strip().lower()) :
            weight1 = 10
            uri[0] = prop.prop_uri
            print "GOT EQUAL"
        else :    
            #Split the relation
            rel_words = q_rels.head.split(" ")
            print "\n", rel_words
            
            sim_vector = []
            if len(rel_words)>1 :
                spec_word_weight = 0
                for word in rel_words :
                    this_weight = lev_similarity(word,prop.label)
                    if this_weight == 1:
                        print "GOT ONE IS EQUAL TO PREDICATE"
                        spec_word_weight = 5
                    else :
                        if this_weight>spec_word_weight :
                            spec_word_weight = this_weight
                sim_vector.append(spec_word_weight)
            else:
                print "Only one word relation"
                sim_vector.append(lev_similarity(q_rels.head,prop.label))
                
            sim_vector.append(size_intersection(q_bag,prop.annotations["bag_of_words"]))
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