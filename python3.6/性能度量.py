# -*- coding: utf-8 -*-
"""
Created on Thu May 25 16:27:05 2017

@author: wangxj
"""

from timeit import Timer
print ('%0.3f' % Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
print ('%0.3f' % Timer('a,b = b,a', 'a=1; b=2').timeit())