# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 16:03:35 2016

@author: wangxj
"""
# Filename: guessnum1.py 
from random import randint 
x = randint(0, 300) 
print 'Please input a number between 0~300:' 
digit = input() 
if digit == x : 
    print 'Bingo!' 
elif digit > x: 
    print 'Too large,please try again.' 
else: print 'Too small,please try again.'