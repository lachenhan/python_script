#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 16:26:42 2021

@author: xiao
"""

name = "mbox-short.txt"
handle = open(name)

    
count = 0
counts = dict()

handle = open(name)
for line in handle:
    if line.startswith('From') and not line.startswith('From:'): 
        words = line.split()
        word = words[1]
        counts[word] = counts.get(word,0) + 1
print(counts.items())

bigcount = None
bigadress = None
for key,value in counts.items():
    if bigcount is None or value > bigcount:
        bigcount  = value
        bigadress = key

    
    
print(bigadress, bigcount)
