#!/usr/bin/env python
# -*- coding:utf-8 -*-
#win7中文版64位运行通过；
#计算程序运行时间
import time
import pandas as pd
import os
start =time.clock()
#改变活动目录，r代表转义字符不生效
os.chdir(r"D:\workspace\salenum") 
#print os.getcwd()
#获取目录下所有csv文件，并打印数量；
filenames = [x for x in os.listdir(os.getcwd()) if x.endswith('csv')]
#print len(filenames)
#创建空DataFrame，并罗列汇总所有记录
df=pd.DataFrame()
print '--'*20
#num=0
for file in filenames:
    dftemp = pd.read_csv(file,header=0,index_col=0,na_values=['NA'])
    print file,"  ",dftemp.shape
    #print dftemp.columns[:3]
    #num=dftemp.index.size+num
    df=pd.concat([dftemp,df])
#print num
print "df.shape after concat: ",df.shape
df=df[['卡号(card_bn)','卡类型(card_type)','地区名称(region_name)','油品名称(oil_name)','购买单价(buy_price)','购买金额(payout)','卡升数(card_litre)', '赠送升数(give_litre)','累计兑付升数(total_cash_litre)','剩余升数(remain_litre)','生成时间(create_time)']]
df=df[df['卡类型(card_type)'].isin(["大众储油体验卡","大众储油卡","1年储油卡","2年储油卡","3年储油卡"])]
print "df.shape after card_type filter: ",df.shape

#print df['卡类型(card_type)'].value_counts()

#体验卡1元特权与油价无关，需要删除;促销价的油品名称需要更改；
df=df[df['油品名称(oil_name)']!='1元特权']
df.loc[df['油品名称(oil_name)'].isin(['促销95#0119','促销95#0129', '促销95#0208','促销95#0218','促销汽油95#']),'油品名称(oil_name)'] = 'Ⅴ汽油95#'
df.drop_duplicates(inplace=True)
print "df.shape after oil_name filter: ",df.shape
#freq=1
for i in range(len(df.index)):
    if (df.iat[i,1]=='1年储油卡') or (df.iat[i,1]=='2年储油卡')or(df.iat[i,1]=='3年储油卡'):
            #print freq," ",i," 卡升数 ",df.iat[i,6]
            df.iat[i,6]=df.iat[i,5]/df.iat[i,4]
            #print freq," ",i," 卡升数 ",df.iat[i,6]
            #freq=freq+1
#df.groupby(['卡类型(card_type)'])['卡升数(card_litre)'].sum()
#df[df['卡类型(card_type)'].isin(['1年储油卡'])]['卡升数(card_litre)'].sum()
df['剩余升数(remain_litre)']=df['卡升数(card_litre)']+df['赠送升数(give_litre)']-df['累计兑付升数(total_cash_litre)']
#生成时间字符串变为时间
#df['生成时间(create_time)']=pd.to_datetime(df['生成时间(create_time)'])
for i in range(df.index.size):
    df.iat[i,-1]=time.strftime("%Y%m%d",time.strptime(df.iat[i,-1],'%Y-%m-%d %H:%M'))
df['销售合计升数']=df['卡升数(card_litre)']+df['赠送升数(give_litre)']
print "df.shape : ",df.shape
###########
os.chdir(r"D:\workspace")
df.to_csv('saledetail.csv',index=False)
###################
#生成用于连接的dataframe
dfgb=df.groupby(['生成时间(create_time)','卡类型(card_type)','地区名称(region_name)','油品名称(oil_name)'])['购买金额(payout)','销售合计升数'].sum().reset_index()
dfgb.columns=['日期', '卡类型(card_type)', '地区名称(region_name)','油品名称(oil_name)', '金额', '数量']
dfgb['交易方向']='销售'
dfmerge=df.loc[:,['卡号(card_bn)', '卡类型(card_type)', '地区名称(region_name)','油品名称(oil_name)',]]
#print "dfgb.columns: ",dfgb.columns
print "dfgb.shape： ",dfgb.shape
print "dfmerge.shape： ",dfmerge.shape
print '--'*20
#加载兑付表格,计算兑付情况，不跟踪到销售订单；
os.chdir(r"D:\workspace\cash") 
#print os.getcwd()
#获取目录下所有csv文件，并打印数量；
filenames = [x for x in os.listdir(os.getcwd()) if x.endswith('csv')]
#print len(filenames)
#创建空DataFrame，并罗列汇总所有记录
dfcash=pd.DataFrame()

for file in filenames:
    dftemp = pd.read_csv(file,header=0,index_col=None,na_values=['NA'])
    print file,"  ",dftemp.shape
    #print dftemp.columns[:3]
    dfcash=pd.concat([dftemp,dfcash])
print "dfcash.shape after contact:",dfcash.shape
#筛选兑付
dfcash=dfcash.iloc[:,[0,3,4,5,10]]
dfcash=dfcash[dfcash.iloc[:,1]=='兑付']
print "df.shape after first time filter: ",df.shape
dfcash.columns=['卡号(card_bn)', '交易方向', '数量','金额','日期']
'''
#导出文件述职字段竟然有单引号，删除；
#dfcash1=dfcash
for i in range(len(dfcash.index)):
    if isinstance(dfcash.iat[i,2],str):
        #print i
        dfcash.iat[i,2]=float(dfcash.iat[i,2].lstrip("'"))
    #else:
        #print "i: ", i," ",dfcash.iat[i,4]
        #dfcash.iat[i,2]=float(dfcash.iat[i,2][1:])
        #dfcash.iat[i,2]=dfcash.iat[i,2].replace("'","")
for i in range(len(dfcash.index)):
    if isinstance(dfcash.iat[i,2],str):
        print "i: ", i," ",dfcash.iat[i,4] 
        
#dfcash2=dfcash
print "dfcash.shape after filter: ",dfcash.shape
'''
for i in range(dfcash.index.size):
    dfcash.iat[i,-1]=time.strftime("%Y%m%d",time.strptime(dfcash.iat[i,-1],'%Y-%m-%d %H:%M'))

dfcash=pd.merge(dfcash,dfmerge,how='left', on='卡号(card_bn)')
print "dfcash.shape after merge: ",dfcash.shape
#########
dfcash1=dfcash
#############
#消费卡之类的兑付无法merge
dfcash=dfcash.dropna()
print "dfcash.shape after dropna: ",dfcash.shape
dfcash=dfcash.groupby(['日期','卡类型(card_type)', '地区名称(region_name)', '油品名称(oil_name)','交易方向'])['数量','金额'].sum().reset_index()
print "dfcash.shape after groupby: ",dfcash.shape
dfall=pd.concat([dfgb,dfcash])
print "dfall.shape after concat: ",dfall.shape

#加载单价表格
os.chdir(r"D:\workspace") 
dfprice = pd.read_csv('price.csv',header=0,index_col=None,na_values=['NA'])
print "dfprice.columns: ",dfprice.columns
#合并
dfall=pd.merge(dfall,dfprice,how='left', on=None,left_on=['地区名称(region_name)','油品名称(oil_name)'],right_on=['城市', '油品类型'])
print "dfall.shape after merge: ",dfall.shape

############
#导出明细数据
dfcash1=pd.merge(dfcash1,dfprice,how='left', on=None,left_on=['地区名称(region_name)','油品名称(oil_name)'],right_on=['城市', '油品类型'])
os.chdir(r"D:\workspace") 
dfcash1.to_csv('cashdetail.csv',index=False)
##############

dfall=dfall.loc[:,['日期','卡类型(card_type)', '地区名称(region_name)', '油品名称(oil_name)','交易方向','金额', '数量','当前单价']]
print "dfall.shape after filter: ",dfall.shape
dfall=dfall.sort_values(['日期', '卡类型(card_type)', '地区名称(region_name)', '油品名称(oil_name)'])
dfall['当前金额']=dfall['数量']*dfall['当前单价']
os.chdir(r"D:\workspace") 
dfall.iloc[:,:].to_csv('allrecord.csv',index=False)


end=time.clock()
print "Running duration: %f s" % (end-start)












