# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 10:43:18 2017

@author: wangxj
"""

from urllib.request import urlopen
with urlopen('http://www.baidu.com') as response:
    for line in response:
        line = line.decode('utf-8')  # Decoding the binary data to text.
        if 'EST' in line or 'EDT' in line:  # look for Eastern Time
            print ( line )