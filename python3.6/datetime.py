# -*- coding: utf-8 -*-
"""
Created on Fri May 26 14:35:40 2017

@author: wangxj
"""

#print (list(range(30,1,-1)))
#获取当前日期和时间
from datetime import datetime
now = datetime.now() # 获取当前datetime
print ('-'*20)
print("now:",now)
#制定日期和时间
dt = datetime(2017, 5, 27, 17, 15) # 用指定日期时间创建datetime
print(dt)
#时间转为时间戳
print(dt.timestamp())

dt = datetime(1970,1,3, 0, 0) # 用指定日期时间创建datetime
print("epoch time: ",dt.timestamp())

#时间戳转为时间
t = 1495876500.0
print (datetime.fromtimestamp(t)) 
print(datetime.utcfromtimestamp(t)) # UTC时间

cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

#print(now + timedelta(days=2, hours=12))
print(now.strftime('%a, %b %d %H:%M'))
