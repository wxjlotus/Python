# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 11:32:45 2017

@author: wangxj

使用蒙特卡洛方法，随机抽样方法计算圆周率pi

"""

# pi.py
from random import random
from math import sqrt
import time
DARTS = 1200
hits = 0
start =time.clock()
for i in range(1,DARTS):
    x, y = random(), random()
    dist = sqrt(x**2 + y**2)
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits/DARTS)
print("the value of Pi is: %.3s" % pi)
end=time.clock()
print ("Running duration: %.3f s" % (end-start))