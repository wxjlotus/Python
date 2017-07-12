#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#win7中文版64位运行通过；
#计算程序运行时间
import time
import pandas as pd
import os
start =time.clock()
#打印行号
import sys
def lineno():
    try:raise Exception
    except:f = sys.exc_info()[2].tb_frame.f_back
    return f.f_lineno
#print ("line num: ",lineno())

localtime = time.localtime(time.time())
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

#加载单价表格
os.chdir(r"D:\workspace") 
#price = pd.read_excel('price.xlsx',header=0,index_col=None,na_values=['NA'])
dfprice = pd.read_csv('price20170626.csv',header=None,index_col=None,na_values=['NA'],skiprows=1)
print (lineno(),"dfprice.shape:",dfprice.shape)
#print (lineno(),dfprice.head())
#取前四列，更换列名，删除城市中的多余字符，保留城市名称，删除重复行；
dfprice=dfprice.loc[:,0:3]
dfprice.columns=[['当前日期','城市','油品类型','当前单价']]
print (lineno(),"dfprice.shape:",dfprice.shape)
#print (lineno(),dfprice.head())

dfprice['城市']=dfprice['城市'].str.replace('\S+/','').str.replace(':\S+','')

'''
dfprice.drop_duplicates(subset=['城市', '油品类型'],inplace=True)
print (lineno(),"dfprice.shape:",dfprice.shape)
#print (lineno(),dfprice.head())



os.chdir(r"D:\workspace") 
#file = "PL"+str(time.strftime("%Y-%m-%d", time.localtime())) + ".xlsx"
file = str("price") + ".xlsx"
dfprice.to_excel(file,index=False)
'''



end=time.clock()
print ("Running duration: %f s" % (end-start))












