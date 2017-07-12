# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 15:46:23 2017

@author: wangxj
"""
import re
m=re.search(r'[1-9]\d{5}','dfsda100810 fdgdf100541')
#m=re.findall(r'[1-9]\d{5}','dfsda100810 fdgdf100541')
if m:print(m.group(0))
#print(m.string)


match=re.search(r'PY.*?N','PYANBNCNDN')
if match:print(match.group(0))
