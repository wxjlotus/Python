#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#win7中文版64位运行通过；anconda2.7版本；
#csv文件汇总，剔除不需要记录；
#计算程序运行时间
import time
import pandas as pd
import os
start =time.clock()
#改变活动目录，r代表转义字符不生效
#需要提前删除单引号
os.chdir(r"D:\workspace\order") 
#print os.getcwd()
#获取目录下所有csv文件，并打印数量；
filenames = [x for x in os.listdir(os.getcwd()) if x.endswith('csv')]
#创建空DataFrame，并罗列汇总所有记录
df=pd.DataFrame()
localtime = time.localtime(time.time())
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

#num=0
for file in filenames:
    #print ("len(filenames): ",len(filenames))
    dftemp = pd.read_csv(file,header=0,index_col=None,na_values=['NA'])
    dftemp=dftemp[dftemp['商品名称(name)'].isin(["大众储油体验卡","大众储油卡"])]
    dftemp=dftemp[['下单时间(createtime)','商品名称(name)','订单总额(final_amount)','订单实付金额(payed)','订单折扣优惠(discount)','订单现金券减免(cpns_money)','订单油箱抵用金额(goil_money)']]
    df=pd.concat([dftemp,df])
print ("#"*50)  
print ("df.shape after concat: ",df.shape)
print (df[['订单总额(final_amount)', '订单实付金额(payed)','订单现金券减免(cpns_money)','订单油箱抵用金额(goil_money)']].sum()/10000)


#os.chdir(r"D:\workspace") 
#df.to_csv('order.csv',index=False)
#df.to_excel('order.xlsx',index=False)
end=time.clock()
print ("Running duration: %f s" % (end-start))












