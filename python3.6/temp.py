# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 16:17:03 2017

@author: wangxj
"""

#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if( i != k ) and (i != j) and (j != k):
                print (i,j,k)