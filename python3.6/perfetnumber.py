# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 16:13:20 2017

@author: wangxj
"""

#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
from sys import stdout
for j in range(2,1001):
    k = []
    n = -1
    s = j
    for i in range(1,j):
            if j % i == 0:
                n += 1
                s -= i
                k.append(i)
    
    if s == 0:
        print (j)
        for i in range(n):
            stdout.write(str(k[i]))
            stdout.write(' ')
        print (k[n])