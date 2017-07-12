# -*- coding: utf-8 -*-
"""
Created on Wed May 31 17:23:25 2017

@author: wangxj


print ("Hello world!")
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n
foo('0')
"""
import logging
#logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)