#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 16:38:45 2021

@author: xiao
"""

#1. String

fruit = 'banana'
print(fruit[1])
print(len(fruit))

last_letter = fruit[len(fruit) - 1]
print(last_letter)


for char in fruit:
    print(char)
 
    
 # count character
count = 0
for char in fruit:
    if char == 'a' : 
        count = count + 1      
print('Letter a appears' , str(count) , 'times in' , fruit)



'a' in fruit
'z' in fruit

type(fruit)
dir(fruit)
help(str.split)

union = '+'.join(['You', 'Me', 'Us'])
print(union)

help(str.partition)

union.partition('-')

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)