# -*- coding: utf-8 -*-
"""
Created on Thu May 25 16:16:31 2017

@author: wangxj
"""

# -*- coding: UTF-8 -*-

# Filename : test.py
# author by : www.runoob.com

# 九九乘法表
for i in range(1, 10):
        for j in range(1, i+1):
            print('{}x{}={}\t'.format(i, j, i*j), end='')
        print()