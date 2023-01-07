#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 17:32:53 2021

@author: xiao

"""

# Place Flowers

def canPlaceFlowers(flowerbed,n):
    f = len(flowerbed)
    
    if n == 0:
        return True
    
    if f <= 2 and set(flowerbed) != {0}:
        return False 
 
    if set(flowerbed) == {1}:
        return False
    

    if set(flowerbed) == {0} and n <= (f + 1) // 2:
        return True
    if set(flowerbed) == {0} and n > (f + 1) // 2:
        return False
    
    one = []
    for x in range(0,f):
        if flowerbed[x] == 1:
            one.append(x)    
    print(one)
    
    zero = [] 
    zero.append(one[0])
    for y in range(1,len(one)):
        zero.append(one[y]-one[y-1]-1)
    zero.append(f - one[-1]-1)   
    print(zero)
    
    num = 0
    if zero[0]  != 0:
        num = num + zero[0]//2
    if zero[-1] != 0:
        num = num + zero[-1]//2   
    for z in range(1,len(zero)-1):
        if zero[z] >=3:
            num = num + (zero[z] - 1)//2   
    print(num)
    
    if n <= num:
        return True
    else: 
        return False  
    
canPlaceFlowers([0,0,1,0,0,0,0,1,0,1,0,0,0,1,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0],17)



    