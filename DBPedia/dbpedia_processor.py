#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 14:35:54 2017

@author: mulang
"""
import json
from pprint import pprint
#!/usr/bin/env python
import urllib2
import urllib
import json
import pprint
import codecs
import csv

#import sparql
from SPARQLWrapper import SPARQLWrapper, JSON
import time


############################################################################################################
###   WE WANT TO COUNT THE NUMBER OF TRIPPLES FOR EVERY RELATION AND CHECK TYPE OF OBJECTS AND SUBJECTS ####
############################################################################################################

dbpedia_file = "DBPedia_plus_counts"
dbpedia_prd_no_inctances = "DBPedia_counts_ratio"


sparql = SPARQLWrapper("https://dbpedia.org/sparql")
sparql.setUseKeepAlive()

with open(dbpedia_file) as f:
    predicates = csv.reader(f)
    num_preds_with_instances = 0
    # num_preds_without_instances = 54583
    start = True
    i=0




    num_instances=0
    for row in predicates:
        print row
        
        clean_predicates = ""     
        print "\n\nSELECT COUNT(DISTINCT ?s) COUNT(DISTINCT ?o)  WHERE { ?s <"+row[0].strip("'").strip('"')+"> ?o . } "
        
        try : 
            sparql.setQuery("SELECT COUNT(DISTINCT ?s) COUNT(DISTINCT ?o)  WHERE { ?s <"+row[0].strip("'").strip('"')+"> ?o . } ")
            #COUNT(DISTINCT ?s) COUNT(DISTINCT ?o) WHERE {?s <http://dbpedia.org/ontology/spouse> ?o}
            
            #print sparql.query
            sparql.setReturnFormat(JSON)
            results = sparql.query().convert()
        
            #count = 0;
                    
            for result in results["results"]["bindings"]:
                uniq_subs = int(result["callret-0"]["value"])
                uniq_objs = int(result["callret-1"]["value"])
                
            #if(count == 0) : 
            #    pass
                #num_preds_without_instances = num_preds_without_instances +1
                #f = open(dbpedia_prd_no_inctances, 'a') 
                #f.write(str(row)[1:-1] +","+str(count)+"\n")
                #f.close()  
                
            #else :
            num_preds_with_instances = num_preds_with_instances +1
            the_row=""
            j=0
            for r in row :
                if j==0 :
                    the_row = the_row+str(r).strip('"').strip("'")
                else :
                    the_row = the_row+","+str(r).strip('"').strip("'")
                j = j+1
            
            the_row = the_row +","+str(uniq_subs)+","+str(uniq_objs)+"\n" 
                
            clean_predicates = clean_predicates + the_row 
                #print 
                
            print "INSTANTIATED PREDICATES : ",num_preds_with_instances
            print i
                
                #if len(row[1]) < 1 and len(row[2]) < 1 :
                #    sparql.setQuery("SELECT ?s, ?o) WHERE { ?s <"+row[0]+"> ?o . } ")
               #    sparql.setReturnFormat(JSON)
               #     results = sparql.query().convert()
                    
               #print str(row)[1:-1] +","+count+"\n"        
              
            
            #print "Total Number of Predicates are : "+str(clean_predicates)
            
            #THE NEXT TASK HERE IS TO FIND THE TOP 4 CLASS LABELS FOR THE DOMAINS AND RANGES FOR INSTANCES OF THE PREDICATE
            
            #print row[-1]
            #num_instances = num_instances + int(row[-1])
                
            fileObject = open(dbpedia_prd_no_inctances,'a') 
            fileObject.write(clean_predicates)
            fileObject.close()
        except :
            pass
        #if row[0].strip() == 'http://dbpedia.org/property/b\\xc3\\xbcrgermeistertitel' :
        #    start = True
        i=i+1 
    
    #print "FOUND PREDICATES : ",
        
        #print row[0], count   
        #print str(results)
        #i=0
        #for result in results["results"]["bindings"]:
        #    eu_dataset_titles =eu_dataset_titles + result["v"]["value"] + "\n"
        #    if i==limit - 1 :
        #        print("s=" + result["s"]["value"] + "\tv=" + result["v"]["value"])
        #    i=i+1
        
        #print out to the file
        #with codecs.open(eu_datasets_out_file, 'a', encoding='utf-8') as out:  
        #    out.write(eu_dataset_titles)
        #out.close()
    
        #offset = offset + limit
       
    #ALL IS SAID AND DONE : PRINT THE COUNTS
    
    #print "INSTANTIATED PREDICATES : ",num_preds_with_instances, "NONE INSTANTIATED PREDICATES : ",num_preds_without_instances
    #f.close()



#offset = offset + limit
#procedure()
#print time.clock() - t0,
#print("loop over all subjects returned in first query:")
#for result in results["results"]["bindings"]:
#    sparql.setQuery("""
#        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
#        PREFIX dbpedia: <http://dbpedia.org/resource/>
#        SELECT ?p ?o
#        WHERE { <""" + result["s"]["value"] +
#          """> ?p ?o } LIMIT 10""")
#    results2 = sparql.query().convert()
#    for result2 in results2["results"]["bindings"]:
#        print("p=" + result2["p"]["value"] + "\to=" + result2["o"]["value"])




