#!/usr/bin/env python
# -*- coding:utf-8 -*-
#各期货品种合约的乘数、手续费等，用于优矿提取数据。
#计算程序运行时间
import time
#import pandas as pd
#import numpy as np
#import matplotlib
#import os
start =time.clock()


df=DataAPI.FutuGet(exchangeCD=["XSGE","XZCE","CCFX","XDCE"],secID=u"",ticker=u"",contractStatus="L",contractObject=u"",field=u"",pandas="1")
print df.shape
df=df[[u'listDate', u'ticker',u"secShortName",
u'minChgPriceUnit', u'contMultNum', u'contMultUnit', u'tradeMarginRatio', u'lastTradeDate', u'tradeCommiNum',u'tradeCommiUnit', u'contractStatus']]
# df=df[df['contractStatus']=='L']
df.index=df['ticker']
df=df.drop(['ticker'],axis=1)
df=df.filter(regex='^zn\d{4}', axis=0)
df.to_csv(u'product20170105.csv')
df




end=time.clock()
print "Running duration: %f s" % (end-start)





