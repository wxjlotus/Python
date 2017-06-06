#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#win7中文版64位运行通过；anconda2.7版本；
#csv文件汇总，剔除不需要记录，仅限于销售记录；记得更改编码；
#计算程序运行时间
import time
import pandas as pd
import os
start =time.clock()
#改变活动目录，r代表转义字符不生效
#需要提前删除单引号
os.chdir(r"D:\workspace\salenum") 
#print os.getcwd()
#获取目录下所有csv文件，并打印数量；
filenames = [x for x in os.listdir(os.getcwd()) if x.endswith('csv')]
print ("filenames: ",len(filenames))
#创建空DataFrame，并罗列汇总所有记录
df=pd.DataFrame()
localtime = time.localtime(time.time())
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

#num=0
for file in filenames:
    dftemp = pd.read_csv(file,header=0,index_col=0,na_values=['NA'])
    dftemp=dftemp[['卡号(card_bn)','卡类型(card_type)','地区名称(region_name)','油品名称(oil_name)','购买单价(buy_price)','购买金额(payout)','卡升数(card_litre)', '赠送升数(give_litre)','生成时间(create_time)']]
    #卡类型筛选
    dftemp=dftemp[dftemp['卡类型(card_type)'].isin(["大众储油体验卡","大众储油卡"])]
    #print "df.shape after card_type filter: ",df.shape
    #print df['卡类型(card_type)'].value_counts()
    #体验卡1元特权与油价无关，需要删除;促销价的油品名称需要更改；
    dftemp=dftemp[dftemp['油品名称(oil_name)']!='1元特权']
    #print "df.shape after oil_name filter: ",df.shape
    df=pd.concat([dftemp,df])
print ("完整的油价相关销售列表记录数量",df.shape)
print ("df.shape after concat: ",df.shape)
df.loc[df['油品名称(oil_name)'].isin(['促销95#0119','促销95#0129', '促销95#0208','促销95#0218','促销汽油95#']),'油品名称(oil_name)'] = 'Ⅴ汽油95#'
df.drop_duplicates(inplace=True)
print ("df.shape after drop: ",df.shape)

print (df['购买金额(payout)'].sum()/10000)

os.chdir(r"D:\workspace") 
df.iloc[:,:].to_csv('sale2016-20170601.csv',index=True)
#df=df[['卡类型(card_type)','购买成本(cost)', '购买金额(payout)', '赠送升数(give_litre)','赠送金额(give_amount)']]


end=time.clock()
print ("Running duration: %f s" % (end-start))












