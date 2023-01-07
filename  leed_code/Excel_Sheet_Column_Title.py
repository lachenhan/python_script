#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 22:42:33 2021

@author: xiao
"""


def convertToTitle(cn) -> str:
    l = []
    quo = -1
    while quo != 0:           
        re = cn % 26
        if re == 0:
            re = 26
        quo = (cn - re)// 26
        l.append(chr(re + 64))
        cn = quo
    l.reverse()
    output = ''.join(l)
    return output 
    
convertToTitle(52)
