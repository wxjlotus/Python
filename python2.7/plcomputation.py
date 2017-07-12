#!/usr/bin/env python
# -*- coding:utf-8 -*-
#win7中文版64位运行通过；编码问题，price.csv先用excel保存，再用记事本改成utf-8-with bom格式；输出格式，pivottable
#逐笔对冲计算浮动盈亏，数据来源是储油列表、当前价格列表，缺点是储油列表时间不一致，累计兑付金额错误；
#计算程序运行时间
import time
import pandas as pd
#import numpy as np
#import matplotlib
import os
start =time.clock()
#改变活动目录，r代表转义字符不生效
os.chdir(r"D:\workspace\salevalid")
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
#DataFrame基本信息确认    
#print "type(df):",type(df)
#print df.dtypes
#print "df.shape:",df.shape
#print df.head(2)
#print len(df.columns)
#print df.columns[:3]
#print df.describe()
    
#DataFrame整理，保留需要字段,仅保留六种卡类型，
#del df['名称(card_name)']
#df.drop(['日期','城市','油品类型'],axis=1, inplace=True)
#df.pop(['日期','城市','油品类型'],axis=1, inplace=True)

#print "累计兑付金额万元： ",df['累计兑付金额(total_cash_amount)'].sum()/10000
df=df[['卡号(card_bn)','卡类型(card_type)','地区名称(region_name)','油品名称(oil_name)','购买单价(buy_price)','购买金额(payout)','卡升数(card_litre)', '赠送升数(give_litre)','累计兑付升数(total_cash_litre)','累计兑付金额(total_cash_amount)','剩余升数(remain_litre)','生成时间(create_time)']]
#确认卡号的唯一性
print "df.shape: ",df.shape
#计算唯一值的数量
print "df唯一值数量：",len(df['卡号(card_bn)'].value_counts())
df=df[df['卡类型(card_type)'].isin(["大众储油体验卡","大众储油卡"])]
#df=df[df['卡类型(card_type)'].isin(["大众储油体验卡","大众储油卡","1年储油卡","2年储油卡","3年储油卡"])]
print "df.shape after card_type filter: ",df.shape
#df.columns.size
#print "兑付数量吨： ",df['累计兑付升数(total_cash_litre)'].sum()/1270
#print "累计兑付金额万元： ",df['累计兑付金额(total_cash_amount)'].sum()/10000
#print df['卡类型(card_type)'].value_counts()

#体验卡1元特权与油价无关，需要删除;促销价的油品名称需要更改；
df=df[df['油品名称(oil_name)']!='1元特权']
df.loc[df['油品名称(oil_name)'].isin(['促销95#0119','促销95#0129', '促销95#0208','促销95#0218','促销汽油95#']),'油品名称(oil_name)'] = 'Ⅴ汽油95#'
#验证字段数值的唯一性；
'''
print df.duplicated().value_counts()
print len(df.index.value_counts())

print df.index.unique
print len(df.index)
print len(df['卡号(card_bn)'])
print len(df['卡号(card_bn)'].value_counts())
obj.duplicated() 本方法返回一个布尔型 Series，将重复的行标记为 True
obj.drop_duplicates() 本方法直接返回一个去除了重复行的新对象

'''
#df.loc[df['卡号(card_bn)']=="'100000220600036342",:]
#df[df['卡号(card_bn)']=="'100000220600036342"]
#df.drop_duplicates('生成时间(create_time)',keep='first',inplace=True)
#print df.index.size
#df.drop(df.loc[df['卡类型(card_type)'].isin(['1年储油卡','3年储油卡','2年储油卡']),:])

#print len(df['卡号(card_bn)'].value_counts())
#print df.dtypes

#1-3年期的储油卡需要计算升数；
#print len(df.loc[df['卡类型(card_type)'].isin(['1年储油卡','3年储油卡','2年储油卡']),['卡升数(card_litre)']])
'''
#freq=1
for i in range(len(df.index)):
    if (df.iat[i,1]=='1年储油卡') or (df.iat[i,1]=='2年储油卡')or(df.iat[i,1]=='3年储油卡'):
            #print freq," ",i," 卡升数 ",df.iat[i,6]
            df.iat[i,6]=df.iat[i,5]/df.iat[i,4]
            #print freq," ",i," 卡升数 ",df.iat[i,6]
            #freq=freq+1
'''
#df.groupby(['卡类型(card_type)'])['卡升数(card_litre)'].sum()
#df[df['卡类型(card_type)'].isin(['1年储油卡'])]['卡升数(card_litre)'].sum()
#由于有固定期限卡，剩余升数需要再次计算
df['剩余升数(remain_litre)']=df['卡升数(card_litre)']+df['赠送升数(give_litre)']-df['累计兑付升数(total_cash_litre)']
#生成时间字符串变为标准6位
#df['生成时间(create_time)']=pd.to_datetime(df['生成时间(create_time)'])
for i in range(df.index.size):
    df.iat[i,-1]=time.strftime("%Y%m%d",time.strptime(df.iat[i,-1],'%Y-%m-%d %H:%M'))
print "df.shape after oil_name filter: ",df.shape
#print "df.columns: ",df.columns
print "累计兑付金额万元： ",df['累计兑付金额(total_cash_amount)'].sum()/10000
print "df.shape after oil_name filter: ",df.shape
df.drop_duplicates(inplace=True)
print "df.shape after drop_duplicates: ",df.shape
#print "兑付数量吨： ",df['累计兑付升数(total_cash_litre)'].sum()/1270

#加载单价表格
os.chdir(r"D:\workspace") 
dfprice = pd.read_csv('price.csv',header=0,index_col=None,na_values=['NA'])
#dfprice = pd.read_csv('price.csv',header=0,index_col=None,na_values=['NA'],encoding="gb2312")
#dfprice = pd.read_excel('price.xlsx',sheetname=0,header=0,index_col=None,na_values=['NA'])
print "dfprice.columns: ",dfprice.columns
df=pd.merge(df,dfprice,how='left', on=None,left_on=['地区名称(region_name)','油品名称(oil_name)'],right_on=['城市', '油品类型'])
#del df['日期']
print "df.shape after merge: ",df.shape

#已经兑付成本的按照比例算法
id=df['累计兑付升数(total_cash_litre)'] * df['购买金额(payout)']/(df['卡升数(card_litre)']+df['赠送升数(give_litre)'])
df.insert(10,'兑付成本按比例计算',id)
#已经兑付PL的计算
id=df['兑付成本按比例计算']-df['累计兑付金额(total_cash_amount)']
df.insert(11,'已经兑付盈亏',id)
#购买成本的按照比例算法
id=df['剩余升数(remain_litre)'] * df['购买金额(payout)']/(df['卡升数(card_litre)']+df['赠送升数(give_litre)'])
df.insert(12,'未兑付成本按比例计算',id)
#购买成本的按照购买单价算法
id=df['剩余升数(remain_litre)'] * df['购买单价(buy_price)']
df.insert(13,'未兑付成本购买单价',id)

id=df['剩余升数(remain_litre)'] * df['当前单价']
df.insert(14,'当前总额',id)

id=df['未兑付成本按比例计算']- df['当前总额']
df.insert(15,'浮动盈亏',id)

'''
#freq=1
for i in range(df.index.size):
    if (df.iat[i,1]=='1年储油卡'):
        df.iat[i,15]=(df.iat[i,12]-df.iat[i,14])*0.3
    
    elif df.iat[i,1]=='2年储油卡':
        df.iat[i,15]=(df.iat[i,12]-df.iat[i,14])*0.4
    
    elif df.iat[i,1]=='3年储油卡':
        #print freq," ",i," 卡升数 ",df.iat[i,6]
        df.iat[i,15]=(df.iat[i,12]-df.iat[i,14])*0.5
        #print freq," ",i," 卡升数 ",df.iat[i,6]
        #freq=freq+1
    else:
        df.iat[i,15]=(df.iat[i,12]-df.iat[i,14])
'''
df.loc[df['浮动盈亏']>0,'浮动盈亏']=0


id=df['已经兑付盈亏']+df['浮动盈亏']
df.insert(16,'总盈亏',id)
df1=df
print "df.shape after computation: ",df.shape
#print "兑付数量吨： ",df['累计兑付升数(total_cash_litre)'].sum()/1270
print "累计兑付金额万元： ",df['累计兑付金额(total_cash_amount)'].sum()/10000
#可以选择导出明细列表
#df=df.loc[:,['卡号(card_bn)','生成时间(create_time)','卡类型(card_type)','地区名称(region_name)','油品名称(oil_name)','购买单价(buy_price)','购买金额(payout)','卡升数(card_litre)','赠送升数(give_litre)','累计兑付升数(total_cash_litre)','累计兑付金额(total_cash_amount)','兑付成本按比例计算','已经兑付盈亏','剩余升数(remain_litre)','未兑付成本按比例计算','未兑付成本购买单价','当前单价','当前总额','浮动盈亏','总盈亏']]
df=df.loc[:,['卡号(card_bn)','卡类型(card_type)','地区名称(region_name)','油品名称(oil_name)','购买单价(buy_price)','购买金额(payout)','卡升数(card_litre)','赠送升数(give_litre)','累计兑付升数(total_cash_litre)','累计兑付金额(total_cash_amount)','剩余升数(remain_litre)','未兑付成本按比例计算','当前单价','浮动盈亏']]
df.iloc[:,:].to_csv('dfrecord.csv',index=False)
print "Export is done."
#print "sale：%d tons."%((df['卡升数(card_litre)']+df['赠送升数(give_litre)']).sum()/1270)
print "Exposure：%d tons."%(df['剩余升数(remain_litre)'].sum()/1270)
print "Floating PL:%.2f million."%(df['浮动盈亏'].sum()/1000000)
#print df.loc[df['生成时间(create_time)']==time.strftime("%Y%m%d",time.localtime(time.time()-24*60*60))][['卡升数(card_litre)', '赠送升数(give_litre)']].sum()/1270
#汇总数据导出
#print df.groupby(['生成时间(create_time)'])['卡升数(card_litre)','赠送升数(give_litre)'].sum()
#gb=df.groupby(['生成时间(create_time)','卡类型(card_type)','地区名称(region_name)','油品名称(oil_name)'])['购买金额(payout)','卡升数(card_litre)','赠送升数(give_litre)','剩余升数(remain_litre)','未兑付成本按比例计算','未兑付成本购买单价','当前总额','PL'].sum().reset_index()
#gb=df.groupby(['卡类型(card_type)','地区名称(region_name)','油品名称(oil_name)'])['购买金额(payout)', '卡升数(card_litre)', '赠送升数(give_litre)','累计兑付升数(total_cash_litre)', '累计兑付金额(total_cash_amount)', '兑付成本按比例计算','已经兑付盈亏','剩余升数(remain_litre)', '未兑付成本按比例计算', '当前总额','浮动盈亏', '总盈亏'].sum().reset_index()
#print "gb.shape: ",gb.shape
#gb.iloc[:,:].to_csv('df.csv',index=False)

end=time.clock()
print "Running duration: %f s" % (end-start)


'''

需要解决编码问题才能应用
freq=1
for i in range(len(df.index)):
    if (df.ix[i,'卡类型(card_type)']=='1年储油卡') or (df.ix[i,'卡类型(card_type)']=='2年储油卡')or(df.ix[i,'卡类型(card_type)']=='3年储油卡'):
            print freq," ",i," 卡升数 ",df.ix[i,'卡升数(card_litre)']
            df.ix[i,'卡升数(card_litre)']=df.ix[i,'购买金额(payout)']/df.ix[i,'购买单价(buy_price)']
            print freq," ",i," 卡升数 ",df.ix[i,'卡升数(card_litre)']
            freq=freq+1



查询：
df.loc[df['卡类型(card_type)'].isin(['1年储油卡','3年储油卡','2年储油卡']),['卡升数(card_litre)','购买金额(payout)','购买单价(buy_price)']]
df1.loc[lambda df: df.A > 0, :] 
df.sort_values('生成时间(create_time)', axis=0, ascending=True, inplace=True)

新建共同列的方式合并
dfprice.columns=['日期','地区名称(region_name)','油品名称(oil_name)','当前单价']

id=df['地区名称(region_name)'] + df['油品名称(oil_name)']
df.insert(9,'地区油品',id)

id2=dfprice['地区名称(region_name)'] + dfprice['油品名称(oil_name)']
dfprice.insert(4,'地区油品',id2)

#pd.merge(df,dfprice,how='left', on=['地区油品']).head()

编码问题coding problem
print isinstance( df.iat[0,-1], unicode)
print isinstance( dfprice.iat[0,-1], unicode)
print isinstance( df.iat[0,-1], str)
print isinstance( dfprice.iat[0,-1], str)

isinstance( dfprice.iat[0,4], unicode)
isinstance( df.iat[0,9], unicode)
isinstance( df.iat[0,9], str)

import codecs


其他合并方式


dfprice[dfprice['地区油品']=='深圳市Ⅴ柴油0#']['地区油品'].value_counts()
df[df['地区油品']=='深圳市Ⅴ柴油0#']['地区油品'].value_counts()

df[df['地区油品']==dfprice.iat[0,4]]['地区油品'].value_counts()
dfprice[dfprice['地区油品']==df.iat[0,9]]['地区油品'].value_counts()
基于left、right共同的列名称
pd.merge(df,dfprice,how='left', on=['地区名称(region_name)','油品名称(oil_name)'])
基于不同的列名称
pd.merge(df,dfprice,how='left', on=None,left_on=['地区名称(region_name)','油品名称(oil_name)'],right_on=['城市', '油品类型']).head()


pivottable

df=df.applymap(lambda x: '%.2f' % x**2)
print df.groupby(['卡类型(card_type)','油品名称(oil_name)']).sum()
print df.groupby(['卡类型(card_type)','油品名称(oil_name)'])[['购买金额(payout)','卡升数(card_litre)', '赠送升数(give_litre)']].sum()

#导出
df.head(10).to_excel('df.xlsx', sheet_name='Sheet1')
dfprice.to_excel('dfprice.xlsx', sheet_name='Sheet1')
df1.to_csv('df.csv')
'''
















