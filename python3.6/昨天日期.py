# -*- coding: utf-8 -*-
"""
Created on Thu May 25 16:26:12 2017

@author: wangxj
"""

# Filename : test.py
# author by : www.runoob.com

# 引入 datetime 模块
import datetime
def getYesterday(): 
	today=datetime.date.today() 
	oneday=datetime.timedelta(days=1) 
	yesterday=today-oneday  
	return yesterday

# 输出
print(getYesterday())