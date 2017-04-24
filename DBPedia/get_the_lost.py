#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 14:14:28 2017

@author: mulang
"""
refetch_file = os.path.join("to_refetch_counts")
pred_count = os.path.join("DBPedia_pred_counts")
pred_no_inst = os.path.join("DBPedia_pred_no_instances")

difference = ""

with open(pred_no_inst) as no_inst :
    no_inst_pred = no_inst.read()
    print type(no_inst_pred)
    
    with open(refetch_file) as refetch_preds: 
        refetchs = refetch_preds.read()
        
        i=0
        for row in  refetchs:
            print type(row)
            matched = False
            for r in no_inst_pred:
                if str(row).strip() ==  str(r)[:-1]:
                    matched = True
                    print "Matched"
                    break
            
            if not matched :
                
                i=i+1
                print i
                difference = difference + str(row) + "\n"
            
        print i
                

#with open(pred_count ) as inst :
    