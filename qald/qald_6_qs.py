#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 20:23:28 2017

@author: mulang
"""

import json
from pprint import pprint
#!/usr/bin/env python
import urllib2
import urllib
import json
import codecs


qald_file = open("qald.js", "r")
output_file = "qald6.txt"

qald_data = qald_file.read()


new_response_dict = json.loads(qald_data)

i=1
output = ""
for question in new_response_dict['questions'] :
    print i, " : ", question["question"][0]["string"]
    
    output = output + question["question"][0]["string"]+"\n"
    i=i+1

with codecs.open(output_file, 'a', encoding='utf-8') as out:  
    out.write(output)
out.close()

#print new_response_dict