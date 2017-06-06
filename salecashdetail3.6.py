#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#win7中文版64位运行通过；anconda2.7版本；
#日期罗列方式计算盈亏，数据来源是储油列表、交易列表、当前价格列表
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
localtime = time.localtime(time.time())
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print ('-'*20)
#num=0
for file in filenames:
    dftemp = pd.read_csv(file,header=0,index_col=0,na_values=['NA'])
    #num=dftemp.index.size+num
    dftemp=dftemp[['卡号(card_bn)','卡类型(card_type)','地区名称(region_name)','油品名称(oil_name)','购买单价(buy_price)','购买金额(payout)','卡升数(card_litre)', '赠送升数(give_litre)','生成时间(create_time)']]
    #卡类型筛选
    dftemp=dftemp[dftemp['卡类型(card_type)'].isin(["大众储油体验卡","大众储油卡"])]
    #体验卡1元特权与油价无关，需要删除;促销价的油品名称需要更改；
    dftemp=dftemp[dftemp['油品名称(oil_name)']!='1元特权']
    df=pd.concat([dftemp,df])
print ("df.shape after concat: ",df.shape)
df.loc[df['油品名称(oil_name)'].isin(['促销95#0119','促销95#0129', '促销95#0208','促销95#0218','促销汽油95#']),'油品名称(oil_name)'] = 'Ⅴ汽油95#'
df.drop_duplicates(inplace=True)
print ("df.shape after drop: ",df.shape)

#生成用于merge的dataframe
dfmerge=df.loc[:,['卡号(card_bn)', '卡类型(card_type)', '地区名称(region_name)','油品名称(oil_name)',]]
#print ("dfmerge.shape after concat: ",dfmerge.shape)
#print ("dfmerge唯一值的数量:",len(dfmerge['卡号(card_bn)'].value_counts()))
#print (dfmerge.index.size))
dfmerge.drop_duplicates(inplace=True)
print ("dfmerge.shape after drop: ",dfmerge.shape)

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
#df['销售合计升数']=df['卡升数(card_litre)']+df['赠送升数(give_litre)']
#print "df.shape : ",df.shape

'''
#所有的油价相关的销售记录导出
os.chdir(r"D:\workspace")
df.to_csv('saledetail.csv',index=False)
'''
#生成用于contact的dataframe
dfgb=df.groupby(['生成时间(create_time)','卡类型(card_type)','地区名称(region_name)','油品名称(oil_name)'])['购买金额(payout)','卡升数(card_litre)','赠送升数(give_litre)'].sum().reset_index()
dfgb.columns=['日期', '卡类型(card_type)', '地区名称(region_name)','油品名称(oil_name)', '销售金额', '销售升数','赠送升数']
dfgb['交易方向']='销售'
dfgb['销售单价']=dfgb['销售金额']/dfgb['销售升数']

#print ("dfgb.columns: ",dfgb.columns)
print ("dfgb.shape用于contact的dataframe： ",dfgb.shape)
print ('--'*30)
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
    dftemp=dftemp[dftemp['产品名称(product_name)'].isin(["大众储油体验卡","大众储油卡"])]
    dftemp=dftemp[dftemp["交易类型(trade_type)"]=='兑付']
    dftemp=dftemp[['产品名称(product_name)','储油通卡号(card_bn)', '交易类型(trade_type)', '数量(trade_nums)', '金额(income)','交易成功时间(trade_end_time)']]
    #print file,"  ",dftemp.shape
    #print dftemp.columns[:3]
    dfcash=pd.concat([dftemp,dfcash])
print ("dfcash.shape after contact:",dfcash.shape)
dfcash.drop_duplicates(inplace=True)
print ("dfcash.shape after drop_duplicates: ",dfcash.shape)
#筛选兑付
#dfcash=dfcash.iloc[:,[0,3,4,5,10]]
dfcash=dfcash[['储油通卡号(card_bn)', '交易类型(trade_type)', '数量(trade_nums)', '金额(income)','交易成功时间(trade_end_time)']]
dfcash=dfcash[dfcash["交易类型(trade_type)"]=='兑付']
#dfcash=dfcash[dfcash.iloc[:,1]=='兑付']
print ("dfcash.shape after trading type filter: ",dfcash.shape)
dfcash.columns=['卡号(card_bn)','交易方向', '兑付升数','兑付金额','日期']
#print "兑付数量吨： ",dfcash['兑付升数'].sum()/1270
#print "兑付金额万元： ",dfcash['兑付金额'].sum()/10000

'''
dfcash=dfcash.iloc[:,[0,1,3,4,5,10]]
dfcash=dfcash[dfcash.iloc[:,2]=='兑付']
print "dfcash.shape after trading type filter: ",dfcash.shape
dfcash.columns=['卡号(card_bn)','卡类型(card_type)','交易方向', '兑付升数','兑付金额','日期']
print dfcash.loc[dfcash['卡类型(card_type)']=='1年储油卡',:]['兑付升数'].sum()

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

#dfcash2=dfcash
print "dfcash.shape after filter: ",dfcash.shape
'''
for i in range(dfcash.index.size):
    dfcash.iat[i,-1]=time.strftime("%Y%m%d",time.strptime(dfcash.iat[i,-1],'%Y-%m-%d %H:%M'))

#获取卡类型，地区，油品名称
dfcash=pd.merge(dfcash,dfmerge,how='left', on='卡号(card_bn)')

print ("dfcash.shape after merge: ",dfcash.shape)
#print dfcash.dtypes
#匹配不到，不符合dfmerge范围的删除
dfcash=dfcash.dropna()
print ("dfcash.shape after dropna: ",dfcash.shape)

#卡类型筛选
dfcash=dfcash[dfcash['卡类型(card_type)'].isin(["大众储油体验卡","大众储油卡"])]
#dfcash=dfcash[dfcash['卡类型(card_type)'].isin(["大众储油体验卡","大众储油卡","1年储油卡","2年储油卡","3年储油卡"])]
print ("dfcash.shape after card_type filter: ",dfcash.shape)
#print df['卡类型(card_type)'].value_counts()
#体验卡1元特权与油价无关，需要删除;促销价的油品名称需要更改；
dfcash=dfcash[dfcash['油品名称(oil_name)']!='1元特权']
dfcash.loc[dfcash['油品名称(oil_name)'].isin(['促销95#0119','促销95#0129', '促销95#0208','促销95#0218','促销汽油95#']),'油品名称(oil_name)'] = 'Ⅴ汽油95#'
print ("dfcash.shape after oil_name filter: ",dfcash.shape)
#print (dfcash.loc[dfcash['卡类型(card_type)']=='1年储油卡',:]['兑付升数'].sum())
dfcash=dfcash.groupby(['日期','卡类型(card_type)', '地区名称(region_name)', '油品名称(oil_name)','交易方向'])['兑付升数','兑付金额'].sum().reset_index()
dfcash['兑付单价']=dfcash['兑付金额']/dfcash['兑付升数']
print ("dfcash.shape after groupby: ",dfcash.shape)
#print "兑付数量吨： ",dfcash['兑付升数'].sum()/1270
#print "兑付金额万元： ",dfcash['兑付金额'].sum()/10000
dfall=pd.concat([dfgb,dfcash])
print ("dfall.shape after concat: ",dfall.shape)
dfall.fillna(value=0)
print ("销售数量吨： ",dfall['销售升数'].sum()/1270)
print ("兑付数量吨： ",dfall['兑付升数'].sum()/1270)
print ("未兑付数量吨： ",dfall['销售升数'].sum()/1270+dfall['赠送升数'].sum()/1270-dfall['兑付升数'].sum()/1270)
print ("兑付金额万元： ",dfall['兑付金额'].sum()/10000)

#加载单价表格
os.chdir(r"D:\workspace") 
dfprice = pd.read_csv('price.csv',header=0,index_col=None,na_values=['NA'])
#print ("dfprice.columns: ",dfprice.columns)
#合并
dfall=pd.merge(dfall,dfprice,how='left', on=None,left_on=['地区名称(region_name)','油品名称(oil_name)'],right_on=['城市', '油品类型'])
print ("dfall.shape after merge: ",dfall.shape)

'''
#导出明细数据
dfcash1=pd.merge(dfcash1,dfprice,how='left', on=None,left_on=['地区名称(region_name)','油品名称(oil_name)'],right_on=['城市', '油品类型'])
os.chdir(r"D:\workspace") 
dfcash1.to_csv('cashdetail.csv',index=False)
'''
dfall=dfall.loc[:,['日期','卡类型(card_type)', '地区名称(region_name)', '油品名称(oil_name)','交易方向', '销售金额','销售升数','销售单价','赠送升数','兑付升数', '兑付金额','兑付单价','当前单价']]
print ("dfall.shape after column filter: ",dfall.shape)
dfall=dfall.sort_values(['日期', '卡类型(card_type)', '地区名称(region_name)', '油品名称(oil_name)'])
#dfall['当前金额']=(dfall['销售升数']+dfall['赠送升数']+dfall['兑付升数'])*dfall['当前单价']

#生成的明细记录数据，写入文件耗时较长，故注释；
#os.chdir(r"D:\workspace") 
#dfall.iloc[:,:].to_csv('alldetail.csv',index=False)

dfall=dfall.fillna(value=0)
dfall['position']=-dfall['销售升数']-dfall['赠送升数']+dfall['兑付升数']
dfall['total PL']=-dfall['销售升数']*(dfall['当前单价']-dfall['销售单价'])-dfall['赠送升数']*dfall['当前单价']+dfall['兑付升数']*(dfall['当前单价']-dfall['兑付单价'])
print ("Position in tons： ",round(dfall['position'].sum()/1270,2))
print ("Total PL in ten thousand: ",round(dfall['total PL'].sum()/10000,2))
#pandas 自带的数据透视表
#table = pd.DataFrame.pivot_table(dfall, values=['销售金额','销售升数','赠送升数','兑付升数', '兑付金额'], index=['日期', '卡类型(card_type)', '地区名称(region_name)', '油品名称(oil_name)','交易方向'],columns=[], aggfunc=sum)
#table=table.reset_index().fillna(value=0).head()
end=time.clock()
print ("Running duration: %f s" % (end-start))












