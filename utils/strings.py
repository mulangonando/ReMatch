#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 06:44:32 2017

@author: mulang
"""
import re

def split_string_on_caps(s) :
    #str_arr = re.split(r'(?<=[a-z])[A-Z]|[A-Z](?=[a-z])', s)
    str_arr = re.findall('([A-Z]?[a-z]+)', s)
    out_str = ''
    for s in str_arr :
        out_str = out_str+s+' '
    out_str.strip()
    return out_str
