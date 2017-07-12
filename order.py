#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#win7中文版64位运行通过；python3.6版本；
#计算程序运行时间
import time
import pandas as pd
import os
start =time.clock()
#改变活动目录，r代表转义字符不生效
os.chdir(r"D:\workspace\order")
#获取目录下所有csv文件，并打印数量；
filenames = [x for x in os.listdir(os.getcwd()) if x.endswith('csv')]
#创建空DataFrame，并罗列汇总所有记录
df=pd.DataFrame()
localtime = time.localtime(time.time())
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print ("len(filenames): ",len(filenames))
for file in filenames:
#    print ("file: ",file)
    dftemp = pd.read_csv(file,header=0,index_col=None,na_values=['NA'])
#    dftemp=dftemp[dftemp['商品名称(name)'].isin(["大众储油体验卡","大众储油卡","大众储油卡(新)","全国加油卡","大众储油节日卡"])]
#    print ("dftemp.shape: ",dftemp.shape)
    dftemp=dftemp[['订单号(order_id)','下单时间(createtime)','订单状态(status)','商品名称(name)','订单总额(final_amount)','订单实付金额(payed)','订单折扣优惠(discount)','订单现金券减免(cpns_money)','订单油箱抵用金额(goil_money)']]
    df=pd.concat([dftemp,df])
print ("-"*50)
df=df[df['订单状态(status)']!='已作废']
df['订单号(order_id)']=df['订单号(order_id)'].astype(str)
df['订单号(order_id)']=df['订单号(order_id)'].str.replace('\'','')
print ("df.shape after concat: ",df.shape)
print ("所有产品（理财+实体）：\n",df[['订单总额(final_amount)', '订单实付金额(payed)','订单折扣优惠(discount)','订单现金券减免(cpns_money)','订单油箱抵用金额(goil_money)']].sum()/10000)
print ("-"*50)
df1=df[df['商品名称(name)'].isin(["大众储油体验卡","大众储油卡"])]
print ("油价相关：\n",df1[['订单总额(final_amount)', '订单实付金额(payed)','订单折扣优惠(discount)','订单现金券减免(cpns_money)','订单油箱抵用金额(goil_money)']].sum()/10000)
print(df['商品名称(name)'].nunique())



#df['商品名称(name)'].value_counts().to_csv("arr.csv")
#分卡类别优惠
#df2=df[['订单总额(final_amount)', '订单实付金额(payed)','订单折扣优惠(discount)','订单现金券减免(cpns_money)','订单油箱抵用金额(goil_money)']].groupby(df['商品名称(name)']).sum()/10000
#df2.to_excel("df.xlsx")
#df.groupby('商品名称(name)').sum()


#df['下单时间(createtime)']=pd.to_datetime(df['下单时间(createtime)'])
#df=df[df['下单时间(createtime)']>=pd.Timestamp('2017-07-01')]
#df=df[df['下单时间(createtime)']<pd.Timestamp('2017-07-03')]
#print (df[['订单实付金额(payed)']].sum()/10000)


#os.chdir(r"D:\workspace")
#df.to_csv('order.csv',index=False)
#df.to_excel('order.xlsx',index=False)



end=time.clock()
print ("Running duration: %f s" % (end-start))












