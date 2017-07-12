# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 16:46:39 2017

@author: wangxj
"""

from turtle import *
color('red', 'blue')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

'''
#画心形
import matplotlib.pyplot as plt
import numpy as np
t = np.arange(0,2*np.pi, 0.1)
x = 16*np.sin(t)**3
y = 13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)
plt.plot(x,y)
'''