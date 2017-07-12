#!/usr/bin/env python
# -*- coding:utf-8 -*-
#各期货品种活跃合约的价格梯度分布
#计算程序运行时间
import time
import pandas as pd
#import numpy as np
#import matplotlib
import os
start =time.clock()

#改变活动目录，r代表转义字符不生效
os.chdir(r"D:\workspace\day")
#print os.getcwd()
#获取目录下所有csv文件，并打印数量；
filenames = [x for x in os.listdir(os.getcwd()) if x.endswith('csv')]
#print len(filenames)
#创建空DataFrame，并罗列汇总所有记录
df=pd.DataFrame()
print '--'*7
for file in filenames:
    dftemp = pd.read_csv(file,header=0,index_col=0,na_values=['NA'])
    #print file,"  ",dftemp.shape
    #print dftemp.columns[:3]
    df=pd.concat([dftemp,df])

#time.sleep(3)

df=df[[u'ticker', u'tradeDate',
       u'contractMark', u'closePrice',
       u'settlePrice', u'turnoverVol', u'openInt',u'mainCon']].fillna(value='')
print 'df.shape: ',df.shape
#print df[df['mainCon']==1].count()
#计算唯一值的数量
print "the number of unique values：",len(df['ticker'].value_counts())
#print "the number of unique values：",len(df['ticker'].unique())
df.index=df['ticker']
df=df.drop(['ticker','contractMark','tradeDate'],axis=1)

#删除无交易量的合约
df=df[df['turnoverVol']>100]
#正则表达式筛选regular expression
df=df.filter(regex='^zn\d{4}', axis=0)
#df['spread']=df['settlePrice']-df.iat[0,1]
id=df['settlePrice']-df.iat[0,1]
df.insert(0,'spread',id)
#print df[df.openInt == df.openInt.max()]
#df.sort_values('turnoverVol', axis=0, ascending=False, inplace=False, kind='quicksort', na_position='last').head(2)
print df
#df.filter(like='i', axis=0)

ax = df.plot(x=None, y=['spread'], kind='bar',color='g', figsize=(10, 5),use_index=True,grid=True)



end=time.clock()
print "Running duration: %f s" % (end-start)
















