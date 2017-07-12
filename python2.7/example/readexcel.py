#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
start =time.clock()

import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt

filename = 'D:\workspace\sale.xlsx'  
#filename = 'D:\workspace\sample-salesv3.xlsx'   
df = pd.read_excel(filename, sheetname=0,header=0,index_col=0,na_values=['NA'])
#df = pd.read_excel(filename, 'Sheet1',header=0,index_col=none,na_values=['NA'])
print type(df)
print df.dtypes
print df.shape
#print df.columns
print df.describe()
print "lenth:  ",len(df.index)

#df['date'] = pd.to_datetime(df['date'])

print df.head(3)
#print df.tail(3)

'''
for i,row in enumerate(range(rows)):
    if i < 10 and i>3:
        value = sheet.row_values(row)
        print i,value
'''
#print "Order by column names, descending:"
#print df.sort_index(axis=1, ascending=False).head()

end=time.clock()
print "Running duration: %f s" % (end-start)