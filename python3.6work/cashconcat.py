#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#win7中文版64位运行通过；anconda2.7版本；
#汇总交易列表，只保留兑付
#计算程序运行时间
import time
import pandas as pd
import os
start =time.clock()

localtime = time.localtime(time.time())
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print ("--"*20)

#加载兑付表格;
os.chdir(r"D:\workspace\cashall") 
#print os.getcwd()
#获取目录下所有csv文件，并打印数量；
filenames = [x for x in os.listdir(os.getcwd()) if x.endswith('csv')]
#print len(filenames)
#创建空DataFrame，并罗列汇总所有记录
dfcash=pd.DataFrame()
for file in filenames:
    dftemp = pd.read_csv(file,header=0,index_col=None,na_values=['NA'])
    dftemp=dftemp[dftemp['产品名称(product_name)'].isin(["大众储油体验卡","大众储油卡","大众储油卡(新)"])]
    dftemp=dftemp[dftemp["交易类型(trade_type)"]=='兑付']
    dftemp=dftemp[['产品名称(product_name)','储油通卡号(card_bn)', '交易类型(trade_type)', '数量(trade_nums)', '金额(income)','交易成功时间(trade_end_time)']]
    #print file,"  ",dftemp.shape
    #print dftemp.columns[:3]
    dfcash=pd.concat([dftemp,dfcash])
print ("dfcash.shape after contact:",dfcash.shape)
print (dfcash['金额(income)'].sum()/10000)
dfcash.drop_duplicates(inplace=True)
print ("dfcash.shape after drop_duplicates: ",dfcash.shape)
print (dfcash['金额(income)'].sum()/10000)

os.chdir(r"D:\workspace") 
dfcash.to_csv('cash2016-20170620.csv',index=False)


end=time.clock()
print ("Running duration: %f s" % (end-start))












