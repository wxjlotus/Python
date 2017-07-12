#!/usr/bin/env python
# -*- coding:utf-8 -*-
#win7中文版64位运行通过；
#逐笔对冲管理方式计算盈亏，数据来源是储油列表、交易列表、当前价格列表，根据卡号匹配；
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
#print df.index.size
#计算唯一值的数量
#print "df唯一值数量：",len(df['卡号(card_bn)'].value_counts())
#print len(df['卡号(card_bn)'].unique())
df=df[['卡号(card_bn)','卡类型(card_type)','地区名称(region_name)','油品名称(oil_name)','购买单价(buy_price)','购买金额(payout)','卡升数(card_litre)', '赠送升数(give_litre)','生成时间(create_time)']]

#df['卡号(card_bn)']=str(df['卡号(card_bn)'])
#卡类型筛选
df=df[df['卡类型(card_type)'].isin(["大众储油体验卡","大众储油卡"])]
print "df.shape after card_type filter: ",df.shape
#print df['卡类型(card_type)'].value_counts()
#体验卡1元特权与油价无关，需要删除;促销价的油品名称需要更改；
df=df[df['油品名称(oil_name)']!='1元特权']
df.loc[df['油品名称(oil_name)'].isin(['促销95#0119','促销95#0129', '促销95#0208','促销95#0218','促销汽油95#']),'油品名称(oil_name)'] = 'Ⅴ汽油95#'
print "df.shape after oil_name filter: ",df.shape
df.drop_duplicates(inplace=True)
print "df.shape after drop唯一值的数量: ",df.shape
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
#生成时间字符串变为时间
#df['生成时间(create_time)']=pd.to_datetime(df['生成时间(create_time)'])

for i in range(df.index.size):
    df.iat[i,-1]=time.strftime("%Y%m%d",time.strptime(df.iat[i,-1],'%Y-%m-%d %H:%M'))
df['销售合计升数']=df['卡升数(card_litre)']+df['赠送升数(give_litre)']
print "df.shape : ",df.shape
print "销售数量吨： ",df['销售合计升数'].sum()/1270
print '--'*30


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
print dfcash.dtypes
#筛选兑付

dfcash=dfcash.iloc[:,[0,3,4,5]]
#print "1兑付数量吨： ",dfcash['数量(trade_nums)'].sum()/1270
#print "1兑付金额万元： ",dfcash['金额(income)'].sum()/10000
#风险点，交易类型的选择
dfcash=dfcash[dfcash.iloc[:,1]=='兑付']
print "dfcash.shape after trading type filter: ",dfcash.shape
dfcash.columns=['卡号(card_bn)', '交易方向', '兑付升数','兑付金额']
#dfcash['卡号(card_bn)']=str(dfcash['卡号(card_bn)'])
print dfcash.dtypes

'''
#导出文件值字段竟然有单引号，删除；
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
        
'''

dfcash=dfcash.groupby(['卡号(card_bn)'])['兑付升数','兑付金额'].sum().reset_index()
dfcash['兑付单价']=dfcash['兑付金额']/dfcash['兑付升数']
print "dfcash.shape after groupby: ",dfcash.shape
#print "兑付数量吨： ",dfcash['兑付升数'].sum()/1270
#print "兑付金额万元： ",dfcash['兑付金额'].sum()/10000
df=pd.merge(df,dfcash,how='left',on=['卡号(card_bn)'])
print "df.shape after concat: ",df.shape
df.fillna(value=0)
print "销售数量吨： ",df['销售合计升数'].sum()/1270
print "兑付数量吨： ",df['兑付升数'].sum()/1270
print "兑付金额万元： ",df['兑付金额'].sum()/10000



#加载单价表格
os.chdir(r"D:\workspace") 
dfprice = pd.read_csv('price.csv',header=0,index_col=None,na_values=['NA'])
print "dfprice.columns: ",dfprice.columns
#合并
df=pd.merge(df,dfprice,how='left', on=None,left_on=['地区名称(region_name)','油品名称(oil_name)'],right_on=['城市', '油品类型'])
print "df.shape after merge: ",df.shape

print "销售数量吨：2 ",df['销售合计升数'].sum()/1270
print "兑付数量吨：2 ",df['兑付升数'].sum()/1270
print "兑付金额万元：2 ",df['兑付金额'].sum()/10000

#列筛选

df=df.loc[:,['卡号(card_bn)','生成时间(create_time)','卡类型(card_type)', '地区名称(region_name)', '油品名称(oil_name)','购买金额(payout)','卡升数(card_litre)','购买单价(buy_price)','赠送升数(give_litre)','兑付升数', '兑付金额','兑付单价','当前单价']]

#主体的计算

id=df['卡升数(card_litre)']+df['赠送升数(give_litre)']-df['兑付升数']
df.insert(10,'剩余升数',id)

df.fillna(value=0)
#df['剩余升数']=df['卡升数(card_litre)']+df['赠送升数(give_litre)']-df['兑付升数']
print "df.shape after filter 2: ",df.shape
print "sale：%d tons."%((df['卡升数(card_litre)']+df['赠送升数(give_litre)']).sum()/1270)
print "cash：%d tons."%(df['兑付升数'].sum()/1270)
print "Exposure：%d tons."%(df['剩余升数'].sum()/1270)
#已经兑付成本的按照比例算法
id=df['兑付升数'] * df['购买金额(payout)']/(df['卡升数(card_litre)']+df['赠送升数(give_litre)'])
df.insert(10,'兑付成本按比例计算',id)
print "df.shape after filter 3: ",df.shape
#已经兑付PL的计算
id=df['兑付成本按比例计算']-df['兑付金额']
df.insert(11,'Realised profit and loss',id)
print "df.shape after filter 4: ",df.shape
#购买成本的按照比例算法
id=df['剩余升数'] * df['购买金额(payout)']/(df['卡升数(card_litre)']+df['赠送升数(give_litre)'])
df.insert(12,'未兑付成本按比例计算',id)
print "df.shape after filter 5: ",df.shape
#购买成本的按照购买单价算法
id=df['剩余升数'] * df['购买单价(buy_price)']
df.insert(13,'未兑付成本按销售单价计算',id)
print "df.shape after filter 6: ",df.shape
id=df['剩余升数'] * df['当前单价']
df.insert(14,'当前总额',id)
print "df.shape after filter 7: ",df.shape

id=df['未兑付成本按比例计算']- df['当前总额']
df.insert(15,'Floating profit and loss',id)
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
df.loc[df['Floating profit and loss']>0,'Floating profit and loss']=0
print "df.shape after filter 8: ",df.shape


id=df['Realised profit and loss']+df['Floating profit and loss']
df.insert(16,'Total PL',id)


#排序
df=df.sort_values(['卡号(card_bn)','卡类型(card_type)', '地区名称(region_name)', '油品名称(oil_name)'])
#index = ['日期','卡号(card_bn)', '卡类型(card_type)', '地区名称(region_name)','油品名称(oil_name)','购买金额(payout)', '卡升数(card_litre)','购买单价(buy_price)', '赠送升数(give_litre)', '兑付升数', '兑付金额', '兑付单价','当前单价','剩余升数']
#df.reindex(index)

os.chdir(r"D:\workspace") 
df.iloc[:,:].to_csv('alldetail.csv',index=False)

print "sale：%d tons."%((df['卡升数(card_litre)']+df['赠送升数(give_litre)']).sum()/1270)
print "cash：%d tons."%(df['兑付升数'].sum()/1270)
print "Exposure：%d tons."%((df['剩余升数']).sum()/1270)
print "Floating PL:%.2f million."%(df['Floating profit and loss'].sum()/1000000)
print "Realised  PL:%.2f million."%(df['Realised profit and loss'].sum()/1000000)
#table = pd.DataFrame.pivot_table(df, values=['销售金额','销售升数','赠送升数','兑付升数', '兑付金额'], index=['日期', '卡类型(card_type)', '地区名称(region_name)', '油品名称(oil_name)','交易方向'],columns=[], aggfunc=sum)
#table=table.reset_index().fillna(value=0).head()

end=time.clock()
print "Running duration: %f s" % (end-start)












