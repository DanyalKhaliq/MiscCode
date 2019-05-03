#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 15:34:44 2019

@author: danyal
"""

import numpy as np

def isOverlapping(a,b,c,d):
    if d < a:
        return False
    if b < c:
        return False
    else:
        return True
    
print(isOverlapping(1,5,2,6))
print(isOverlapping(1,5,6,8))