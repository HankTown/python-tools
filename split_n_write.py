# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 20:46:26 2019

@author: DHF
"""
import re

f = open('金融学本体.txt', 'rt',encoding='utf-8')
data=f.read()
res=open('res.txt','at',encoding='utf-8')

line_pat=re.compile(r'IRI="#(.*)"')
for content in line_pat.findall(data):
    res.write(content+"\n")
f.close()
res.close()