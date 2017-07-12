#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 11:17:13 2017

a test module

@author: wangxj
"""


__author__ = 'wangxj'

import sys

def test():
    args = sys.argv
    print("args:",args)
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()