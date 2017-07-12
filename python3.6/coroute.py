# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 09:17:02 2017

@author: wangxj
"""

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            print ('n::',n)
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 3:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)