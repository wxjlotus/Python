#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#win7中文版64位运行通过；anconda2.7版本；
#csv文件汇总，剔除不需要记录，仅限于销售记录；
#计算程序运行时间
import time
import pandas as pd
start =time.clock()
#改变活动目录，r代表转义字符不生效
#需要提前删除单引号

df=pd.DataFrame()
localtime = time.localtime(time.time())
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

df = pd.read_csv(r"D:\workspace\salenum\sale2016-20170601.csv",header=0,index_col=0,na_values=['NA'])
print ("df.shape: ",df.shape)



end=time.clock()
print ("Running duration: %f s" % (end-start))












