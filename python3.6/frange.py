# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 16:01:08 2017
#实现了位置参数的花式变换；
@author: wangxj
"""
import math
def frange(start,stop=None,step=1):
    result = []
    if stop==None:
        stop=start
        start=0.0
    if step>=1:
        while start < stop:
            result.append(float(start))
            start +=step
    elif step<=-1:
        while start > stop:
            result.append(float(start))
            start +=step       
    return result
print ("dfall.shape after column filter: {:0.6%}".format(math.pi))