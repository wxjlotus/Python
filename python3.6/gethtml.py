# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 12:40:19 2017

@author: wangxj
"""

import urllib
response=urllib.urlopen('http://www.baidu.com.hk/')
html=response.read()
print (html)