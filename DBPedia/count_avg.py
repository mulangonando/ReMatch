#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 11:37:52 2017

@author: mulang
"""

import csv

############################################################################################################
###   WE WANT TO COUNT THE NUMBER OF TRIPPLES FOR EVERY RELATION AND CHECK TYPE OF OBJECTS AND SUBJECTS ####
############################################################################################################

dbpedia_prd_no_inctances = "DBPedia_counts_ratio"

with open(dbpedia_prd_no_inctances) as f:
    predicates = csv.reader(f)
    sum_instances = 0
    
    i=0
    
    for row in predicates:
        
        try:
            sum_instances = sum_instances + int(row[-3])
        except:
            #print row[0]
            print row[0], "\t",row[0].split(" ")[-1],i
            sum_instances = sum_instances + int(row[0].split(" ")[-1])
            
        i = i+1
    
    print sum_instances, i    
    avg = sum_instances / i
    
    print avg