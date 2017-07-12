#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#win7中文版64位运行通过；anconda2.7版本；不需要删除单引号，
#计算程序运行时间
import time
import pandas as pd
import os
#import sys
start =time.clock()
import sys
def lineno():
    try:raise Exception
    except:f = sys.exc_info()[2].tb_frame.f_back
    return f.f_lineno
#print ("line num: ",lineno())

localtime = time.localtime(time.time())
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

#加载销售列表，
#df = pd.read_csv(r"D:\workspace\salenum\sale2016-20170601.csv",header=0,index_col=0,na_values=['NA'])
#df = pd.read_excel(r"D:\workspace\sale61.xlsx",header=0,index_col=None,na_values=['NA'])
#df = pd.read_csv(r"D:\workspace\sale61.csv",header=0,index_col=None,na_values=['NA'])
#改变活动目录，r代表转义字符不生效
os.chdir(r"D:\workspace\saletest")
#print os.getcwd()
#获取目录下所有csv文件，并打印数量；
filenames = [x for x in os.listdir(os.getcwd()) if x.endswith('csv')]
#print len(filenames)
#创建空DataFrame，并罗列汇总所有记录
df=pd.DataFrame()
#num=0
for file in filenames:
    dftemp = pd.read_csv(file,header=0,index_col=None,na_values=['NA'])
    #num=dftemp.index.size+num
#    dftemp=dftemp[['订单号','卡号(card_bn)','卡类型(card_type)','地区名称(region_name)','油品名称(oil_name)','购买金额(payout)','购买成本(cost)','收益（元）(profit)','生成时间(create_time)']]
    dftemp['订单号']=dftemp['订单号'].astype(str)
    dftemp['订单号']=dftemp['订单号'].str.replace('\'','')
    dftemp['卡号(card_bn)']=dftemp['卡号(card_bn)'].astype(str)
    dftemp['卡号(card_bn)']=dftemp['卡号(card_bn)'].str.replace('\'','')
    #卡类型筛选
#    dftemp=dftemp[dftemp['卡类型(card_type)'].isin(["大众储油体验卡","大众储油卡","大众储油卡(新)"])]
    #体验卡1元特权与油价无关，需要删除;促销价的油品名称需要更改；
#    dftemp=dftemp[dftemp['油品名称(oil_name)']!='1元特权']
    df=pd.concat([dftemp,df])
print (lineno(),"df.shape after concat: ",df.shape)
print (lineno(),"df.index.value_counts()",len(df.index.value_counts()))
#print (df.index.size)
print (df.index.nunique())
print (len(df.index.unique()))
print (lineno(),"len(df['卡号(card_bn)'].unique():",len(df['卡号(card_bn)'].unique()))
print (lineno(),"df['卡号(card_bn)'].value_counts():",len(df['卡号(card_bn)'].value_counts()))
#print (df.dtypes)
#print (dftemp.iat[0,0])
#索引可以与值相互更改；
#df.set_index('订单号',inplace=True)
#df.reset_index(inplace=True)
#print (type(df.iat[0,-1]))
df[u'生成时间(create_time)']=pd.to_datetime(df[u'生成时间(create_time)'])
#print (df['生成时间(create_time)'].describe())
#print (type(df.iat[0,-1]))
df=df[df['生成时间(create_time)']>=pd.Timestamp('2017-05-31')]
df=df[df['生成时间(create_time)']<pd.Timestamp('2017-06-16')]
df['生成时间(create_time)']=df['生成时间(create_time)'].map(pd.Timestamp.date)
print (lineno(),"df.shape after time filter: ",df.shape)
#df.iat[0,-1]>pd.Timestamp('2012-05-01')
#df[df['生成时间(create_time)']>'2017-06-07'].describe()
#df[u'生成时间(create_time)']=df[u'生成时间(create_time)'].dt.strftime('%Y-%m-%d')
df.sort_values(by=[u'生成时间(create_time)'],inplace=True)
print (lineno(),"df.shape after sort ",df.shape)


#df['卡号(card_bn)'].str.contains('^0',na=False).value_counts()
#df[df['地区名称(region_name)']=='NA']

#加载单价表格
#dfprice = pd.read_csv(r'D:\workspace\price.csv',header=0,index_col=None,na_values=['NA'])
#print ("dfprice.columns: ",dfprice.columns)
#dfprice=dfprice.iloc[:,1:3]
#合并
#dfall=pd.merge(df,dfprice,how='left', on=None,left_on=['地区名称(region_name)','油品名称(oil_name)'],right_on=['城市', '油品类型'])
#print ("dfall.shape after merge: ",dfall.shape)
#dfall=dfall.fillna(value=0)
#dfall.isnull?


##################################################################################
#dforder = pd.read_csv(r"D:\workspace\ordertest\order20170614-15.csv",header=0,index_col=None,na_values=['NA'])
'''
os.chdir(r"D:\workspace\ordertest")
#print os.getcwd()
#获取目录下所有csv文件，并打印数量；
filenames = [x for x in os.listdir(os.getcwd()) if x.endswith('csv')]
#创建空DataFrame，并罗列汇总所有记录
dforder=pd.DataFrame()

#num=0
for file in filenames:
    #print ("len(filenames): ",len(filenames))
    dftemp = pd.read_csv(file,header=0,index_col=None,na_values=['NA'])
    #dftemp=dftemp[dftemp['商品名称(name)'].isin(["大众储油体验卡","大众储油卡"])]
    dftemp=dftemp[['订单号(order_id)','下单时间(createtime)','商品名称(name)','订单总额(final_amount)','订单实付金额(payed)','订单折扣优惠(discount)','订单现金券减免(cpns_money)','订单油箱抵用金额(goil_money)']]
    dforder=pd.concat([dftemp,dforder])
print ("#"*50)
print ("dforder.shape after concat: ",dforder.shape)
print ("dforder['订单号(order_id)'].value_counts()",len(dforder['订单号(order_id)'].value_counts()))
print (dforder[['订单总额(final_amount)', '订单实付金额(payed)','订单现金券减免(cpns_money)','订单油箱抵用金额(goil_money)']].sum()/10000)


#加载兑付表格,计算兑付情况，不跟踪到销售订单；
os.chdir(r"D:\workspace\cashtest")
#print os.getcwd()
#获取目录下所有csv文件，并打印数量；
filenames = [x for x in os.listdir(os.getcwd()) if x.endswith('csv')]
#print len(filenames)
#创建空DataFrame，并罗列汇总所有记录
dfcash=pd.DataFrame()
for file in filenames:
    dftemp = pd.read_csv(file,header=0,index_col=None,na_values=['NA'])
    #dftemp=dftemp[dftemp['产品名称(product_name)'].isin(["大众储油体验卡","大众储油卡"])]
    #dftemp=dftemp[dftemp["交易类型(trade_type)"]=='兑付']
    dftemp=dftemp[['产品名称(product_name)','储油通卡号(card_bn)', '交易类型(trade_type)', '数量(trade_nums)', '金额(income)','交易成功时间(trade_end_time)']]
    #print file,"  ",dftemp.shape
    #print dftemp.columns[:3]
    dfcash=pd.concat([dftemp,dfcash])
print ("dfcash.shape after contact:",dfcash.shape)
print (dfcash['金额(income)'].sum()/10000)
#dfcash.drop_duplicates(inplace=True)
#print ("dfcash.shape after drop_duplicates: ",dfcash.shape)
#筛选兑付
#dfcash=dfcash.iloc[:,[0,3,4,5,10]]
#dfcash=dfcash[['储油通卡号(card_bn)', '交易类型(trade_type)', '数量(trade_nums)', '金额(income)','交易成功时间(trade_end_time)']]
#dfcash=dfcash[dfcash["交易类型(trade_type)"]=='兑付']
#dfcash=dfcash[dfcash.iloc[:,1]=='兑付']
#print ("dfcash.shape after trading type filter: ",dfcash.shape)
dfcash.columns=['卡类型','卡号(card_bn)','交易方向', '兑付升数','兑付金额','日期']
#dfcash['交易成功时间(trade_end_time)']=pd.to_datetime(dfcash['交易成功时间(trade_end_time)'])
#dfcash['交易成功时间(trade_end_time)']=dfcash['交易成功时间(trade_end_time)'].map(pd.Timestamp.date)

print (dfcash['兑付金额'].sum()/10000)


'''


end=time.clock()
print ("Running duration: %f s" % (end-start))












