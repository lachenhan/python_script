#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 10:36:58 2021

@author: xiao
"""


# Defanging IP address
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return "[.]".join(self.address.split("."))



# Kids With the Greatest Number of Candies
candies = [2,3,5,1,3]
extraCandies = 3

g = 0
b = 'True'
List = []
for c in candies:
    if c > g: g = c

for c in candies:
    b = c + extraCandies >= g
    List.append(b)
print(List)
     

# Richest Customer Wealth
#Solution 1
accounts = [[1,5],[7,3],[3,5]]
g = 0
for cus in accounts:
    a = 0
    for money in cus:
        a = a + money
    if a > g: g = a   
print(g)        

# Solution 2
accounts = [[1,5],[7,3],[3,5]]
w = []
for i in range (0,len(accounts)):
    agg_w = 0
    for cus_m in accounts[i]:
        agg_w = agg_w + cus_m
    w.append(agg_w)
w.sort(reverse=True)
print(w[0])
        



# Shuffle the Array
nums = [2,5,1,3,4,7]
n = 3
new = []
for i in range(0,n):
    new.append(nums[i])
    new.append(nums[i+n])
print(new)

# OR:
x = nums[:n]
y = nums[n:]
new = []
for i in range(0,n):
    new.append(x[i])
    new.append(y[i])
print(new)


# Buddy Strings
#Given two strings a and b, return true 
#if you can swap two letters in a so the result is equal to b, 
#otherwise, return false.
a = "abbd"
b = "abdc"

def comp(a,b):
    
    if len(a) != len(b):
        return False
    
    
    if a == b:
        if len(list(a)) == len(set(list(a))):
            return False
        else: return True
 
        
    A = list(a)
    B = list(b)
        
    dic_a = {}
    dic_b = {}
    
    for i in A:
        dic_a[i] = dic_a.get(i,0) + 1
    for j in B:
        dic_b[j] = dic_b.get(j,0) + 1
        
    
    if dic_a != dic_b:
        return False
    
    l = []
    same = 'True'
    for x in range(len(a)):
        same = A[x] == B[x]
        l.append(same)
    if l.count(False) == 0 or l.count(False) == 2:
        return True
    else: return False
comp('abcd','abdc')
        

    
    

#  Third Maximum Number
#: List[int] -> int
def thirdMax(nums):
    
    if len(set(nums)) == 1:
        return nums[0]
    if len(set(nums)) == 2:
        return max(nums)
    if len(set(nums)) >= 3:
        x = sorted(set(nums),reverse = True)
        return x[2]
        
    


