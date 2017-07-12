#!/usr/bin/env python
# -*- coding:utf-8 -*-
#计算程序运行时间
import time
import pandas as pd
#import numpy as np
#import matplotlib
import os
start =time.clock()

#改变活动目录，r代表转义字符不生效
os.chdir(r"D:\workspace\trading")
#print os.getcwd()
#获取目录下所有csv文件，并打印数量；
filenames = [x for x in os.listdir(os.getcwd()) if x.endswith('csv')]
#print len(filenames)
#创建空DataFrame，并罗列汇总所有记录
df=pd.DataFrame()
print '--'*7
for file in filenames:
    dftemp = pd.read_csv(file,header=0,na_values=['NA'],parse_dates={'timestamp': ['dataDate','dataTime']},index_col='timestamp')
    #print file,"  ",dftemp.shape
    #print dftemp.columns[:3]
    df=pd.concat([dftemp,df])

#time.sleep(3)
#tick数据获取,多数字段为累计数据
#df=df[['dataDate','dataTime','lastPrice','volume','value','openInterest',u'bidPrice1',u'bidVolume1',u'askPrice1',u'askVolume1']]
df=df[['lastPrice','volume','value','openInterest',u'bidPrice1',u'bidVolume1',u'askPrice1',u'askVolume1']]
print "settlementPrice：",df.ix[df.index.size-1,'value']/df.ix[df.index.size-1,'volume']/100
print "df.index.size: ",df.shape
print "nunique: ",df.index.nunique(dropna=True)
#print len(df.index.unique())
print "total minutes:375 or 225"
print "trading minutes:",df.index.size/60/2
df['volume'] = df.volume - df.volume.shift().fillna(value=0)
df['value'] = df.value - df.value.shift().fillna(value=0)
df['openInterest'] = df.openInterest - df.openInterest.shift().fillna(value=0)
df['avg'] = df['value']/df['volume']/100
#print df['lastPrice'].describe()
#print df[df.lastPrice == df.lastPrice.max()].head()
#print df[df.lastPrice == df.lastPrice.min()].head()
#print df[df.lastPrice == df.lastPrice.min()].index[0]
#字符串转化为日期和时间
df=df[['lastPrice','volume']]
#print df.head(3) 
print "df.lastPrice.max(): ",df.lastPrice.max()
print "df.lastPrice.min(): ",df.lastPrice.min()
#tick数据如何形成K线图形？
df.index=pd.to_datetime(df.index)
dfp=df['lastPrice'].resample('1min').ohlc()
#print dfp.shape
dfp=dfp.dropna()
#print dfp.shape
#print dfp.head(2)

dfv=df['volume'].resample('1min').sum()
dfv=pd.DataFrame(dfv,columns=['volume'])
#print dfv.shape
dfv=dfv.dropna()
#print dfv.shape

#print dfv.head(2)

df=pd.merge(dfp,dfv,how='inner', left_index=True, right_index=True)
print df.shape
print df.head(2)
df['volatility']=df.high-df.low
df1=df[df['volatility']!=0]
print df['volatility'].describe()
print df1['volatility'].describe()

'''
#求最大回撤，最大拉升，对应时间，变化速度，成交量，
drawdown=0
for i in range(len(df.index)):
    #print df.iloc[i:,2].min()
    df1=df.iloc[i:,:]
    if ((df.iloc[i:,2].min()-df.iat[i,2])<drawdown):
        drawdown=df.iloc[i:,2].min()-df.iat[i,2]
        m = i
        drawdown1=df.iat[i,2]
        n=df1[df1.lastPrice == df1.lastPrice.min()].index[0]
        drawdown2=df.iloc[i:,2].min()
        #print "i:",i
print "max drawdown: ",drawdown
print "max drawdown start: ",m
print "max drawdown1: ",drawdown1
print "max drawdown end: ",n
print "max drawdown2: ",drawdown2
#print "max drawdown end: ",n


drawup=0
for i in range(len(df.index)):
    #print df.iloc[i:,2].min()
    df1=df.iloc[i:,:]
    if ((df.iloc[i:,2].max()-df.iat[i,2])>drawup):
        drawup=df.iloc[i:,2].max()-df.iat[i,2]
        m = i
        drawup1=df.iat[i,2]        
        n=df1[df1.lastPrice == df1.lastPrice.max()].index[0]
        drawup2=df.iloc[i:,2].max()
        #print "i:",i
print "max drawup: ",drawup
print "max drawup start: ",m
print "max drawup1: ",drawup1
print "max drawup end: ",n
print "max drawup2: ",drawup2
'''

#print "max drawdown end: ",n


#耗时太长，无实用价值
'''
for i in range(len(df.index)):
    for j in range(i,len(df.index)):
        if ((df.iat[j,2]-df.iat[i,2])<temp):
            temp = df.iat[j,2]-df.iat[i,2]
            m = i
            n = j
            print "i:",i," j: ",j
'''          
            


#time.sleep(3)

#ax = df.plot(x='dataTime', y=['lastPrice'], kind='line',color='g', figsize=(15, 7),grid=True)



#bx = df.plot(x='dataTime', y=['volume'], color='r', figsize=(15, 7))
#cx = df.plot(x='dataTime', y=['openInterest'], color='r', figsize=(15, 7))
#dx = df.plot(x='dataTime', y=['bidVolume1'], color='r', figsize=(15, 7))
#ex = df.plot(x='dataTime', y=['askVolume1'], color='r', figsize=(15, 7))


end=time.clock()
print "Running duration: %f s" % (end-start)