#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 12:00:38 2021

@author: xiao
"""

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    l = line.split()
    for i in l:
        if i not in lst: 
            lst.append(i)
lst.sort()       
print(lst)
