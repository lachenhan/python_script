#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 16:38:45 2021

@author: xiao
"""

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"

count = 0
counts = dict()

handle = open(name)
for line in handle:
    if line.startswith('From') and not line.startswith('From:'): 
        h = line.find(':')
        word = line[(h - 2): h]
        counts[word] = counts.get(word,0) + 1

for (k,v) in sorted(counts.items()):
    print(k,v)
