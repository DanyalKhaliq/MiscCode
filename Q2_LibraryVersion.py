#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 15:47:12 2019

@author: danyal
"""



def versionMatch(v1,v2):
    v1arr = v1.split(".")
    v2arr = v2.split(".")
    t = len(v1arr) if len(v1arr) >= len(v2arr) else len(v2arr)
    
    for x in range(0,t):
        if int(v1arr[x]) > int(v2arr[x]):
            return "V1 > V2"
        if int(v1arr[x]) == int(v2arr[x]):
            continue
        else:
            return "V2 > V1"
        

print(versionMatch("1.0.2","1.0.1"))
print(versionMatch("2.3.1","10.1.2"))
print(versionMatch("2.3.0.1","2.1.0.2"))
