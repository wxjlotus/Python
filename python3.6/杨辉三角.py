# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 16:07:46 2017

@author: Thinkpad
"""

def triangles():
    b = [1]
    while True:
        yield b
        b = [1] + [b[i] + b[i+1] for i in range(len(b)-1)] + [1]
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
    
def triangles():
    a=[1]
    while True:
        yield a
        a=[sum(i) for i in zip([0]+a,a+[0])]
n=0
for t in triangles():
    print(t)
    n=n+1
    if n == 10:
        break