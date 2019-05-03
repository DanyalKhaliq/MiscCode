#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 14:48:44 2019

@author: danyal
"""

from googlesearch import search
from newspaper import Article

 
articles = {}

for url in search('keystone - Circular reference found role inference', tld='com', stop=5):
    data = Article(url)
    data.download()
    data.parse()
    articles[url] = data.text
    

for key,val in articles.items():
    print( key, "=>", val)