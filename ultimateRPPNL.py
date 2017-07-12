#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#win7中文版64位运行通过；
#逐笔对冲管理方式计算盈亏，Realised/paper profit and loss数据来源是储油列表、交易列表、当前价格列表，根据卡号匹配；
#来源于2.7版本的Ultimate
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

#section 1：销售列表处理；
#改变活动目录，r代表转义字符不生效
os.chdir(r"D:\workspace\sale")
#获取当前目录下所有csv文件，并打印数量；
filenames = [x for x in os.listdir(os.getcwd()) if x.endswith('csv')]
#创建空DataFrame，并罗列汇总所有记录
df=pd.DataFrame()
print ('--'*20)
for file in filenames:
    dftemp = pd.read_csv(file,header=0,index_col=None,na_values=['NA'])
    dftemp=dftemp[dftemp['状态(card_status)']!='失效']
    dftemp=dftemp[['卡号(card_bn)','卡类型(card_type)','地区名称(region_name)','油品名称(oil_name)','购买单价(buy_price)','购买金额(payout)','卡升数(card_litre)', '赠送升数(give_litre)','生成时间(create_time)']]
    #卡类型筛选
#    dftemp=dftemp[dftemp['卡类型(card_type)'].isin(["大众储油体验卡","大众储油卡","大众储油卡(新)","全国加油卡","大众储油节日卡"])]
    dftemp=dftemp[dftemp['卡类型(card_type)'].isin(["大众储油体验卡","大众储油卡","大众储油卡(新)"])]
    #体验卡1元特权与油价无关，需要删除;促销价的油品名称需要更改；
    dftemp=dftemp[dftemp['油品名称(oil_name)']!='1元特权']
    dftemp['卡号(card_bn)']=dftemp['卡号(card_bn)'].astype(str)
    dftemp['卡号(card_bn)']=dftemp['卡号(card_bn)'].str.replace('\'','')
    #dftemp['卡号(card_bn)']=dftemp['卡号(card_bn)'].astype(int)
    df=pd.concat([dftemp,df])
print (lineno(),"大众储油卡(新)销售数量：",df[df['卡类型(card_type)']=='大众储油卡(新)'].shape)
df.loc[df['油品名称(oil_name)'].isin(['促销95#0119','促销95#0129', '促销95#0208','促销95#0218','促销汽油95#']),'油品名称(oil_name)'] = 'Ⅴ汽油95#'
#(df['购买金额(payout)']==df['卡升数(card_litre)']*df['购买单价(buy_price)']).value_counts()
df['生成时间(create_time)']=pd.to_datetime(df['生成时间(create_time)'])
df['生成时间(create_time)']=df['生成时间(create_time)'].map(pd.Timestamp.date)
#print (lineno(),"df.shape after concat: ",df.shape)
#print (lineno()," 销售数量吨： ",round(df['卡升数(card_litre)'].sum()/1270,2))
#print (lineno()," 客户购买金额：",round(df['购买金额(payout)'].sum()/10000,2))
#print (lineno(),"赠送数量吨： ",round(df['赠送升数(give_litre)'].sum()/1270,2))
print (lineno(),"销售数量吨： ",round((df['卡升数(card_litre)'].sum()+df['赠送升数(give_litre)'].sum())/1270,2))
#print (lineno(),"赠送金额: ",round((df['赠送升数(give_litre)']*df['购买单价(buy_price)']).sum()/10000,2))
#计算唯一值的数量
#print (lineno(),"df['卡号(card_bn)'].nunique()：",(df['卡号(card_bn)'].nunique()))
#print (lineno(),"len(df['卡号(card_bn)'].unique()",len(df['卡号(card_bn)'].unique()))
#df=df[['卡号(card_bn)','卡类型(card_type)','地区名称(region_name)','油品名称(oil_name)','购买单价(buy_price)','购买金额(payout)','卡升数(card_litre)', '赠送升数(give_litre)','生成时间(create_time)']]
#卡号理论上是唯一的
df.drop_duplicates(inplace=True)
print (lineno(),"df.shape after drop_duplicates: ",df.shape)
#促销价格的存在使得购买金额不一定等于升数与单价乘积
#df[df['购买金额(payout)']!=df['卡升数(card_litre)']*df['购买单价(buy_price)']].head()
#df[df['卡类型(card_type)'].isin(['1年储油卡'])]['卡升数(card_litre)'].sum()
#df['销售合计升数']=df['卡升数(card_litre)']+df['赠送升数(give_litre)']
#print (lineno(),"销售数量吨： ",(df['卡升数(card_litre)'].sum()+df['赠送升数(give_litre)'].sum())/1270)
print (lineno(),'--'*30)


#section 2:加载兑付表格,计算兑付情况；
os.chdir(r"D:\workspace\cash")
#获取目录下所有csv文件；
filenames = [x for x in os.listdir(os.getcwd()) if x.endswith('csv')]
#print (len(filenames))
#创建空DataFrame，并罗列汇总所有记录
dfcash=pd.DataFrame()
for file in filenames:
    dftemp = pd.read_csv(file,header=0,index_col=None,na_values=['NA'])
    dftemp=dftemp[['产品名称(product_name)','储油通卡号(card_bn)', '交易类型(trade_type)', '数量(trade_nums)', '金额(income)','交易成功时间(trade_end_time)']]
    dftemp=dftemp[dftemp['产品名称(product_name)'].isin(["大众储油体验卡","大众储油卡","大众储油卡(新)"])]
    dftemp=dftemp[dftemp["交易类型(trade_type)"]=='兑付']
    dftemp['储油通卡号(card_bn)']=dftemp['储油通卡号(card_bn)'].astype(str)
    dftemp['储油通卡号(card_bn)']=dftemp['储油通卡号(card_bn)'].str.replace('\'','')
    dfcash=pd.concat([dftemp,dfcash])
print (lineno(),"dfcash.shape after contact:",dfcash.shape)
print (lineno()," 兑付金额万元： ",dfcash['金额(income)'].sum()/10000)
print (lineno()," 兑付数量吨： ",dfcash['数量(trade_nums)'].sum()/1270)
#dfcash.drop_duplicates(inplace=True)
#print ("dfcash.shape after drop_duplicates: ",dfcash.shape)
#变更为日期类型
dfcash['交易成功时间(trade_end_time)']=pd.to_datetime(dfcash['交易成功时间(trade_end_time)'])
dfcash['交易成功时间(trade_end_time)']=dfcash['交易成功时间(trade_end_time)'].map(pd.Timestamp.date)
#选择有效列
dfcash=dfcash[['储油通卡号(card_bn)', '交易类型(trade_type)', '数量(trade_nums)', '金额(income)']]
dfcash.columns=['卡号(card_bn)', '交易方向', '兑付升数','兑付金额']
#按照卡号汇总
dfcash=dfcash.groupby(['卡号(card_bn)'])['兑付升数','兑付金额'].sum().reset_index()
#dfcash['兑付单价']=dfcash['兑付金额']/dfcash['兑付升数']
#print (lineno(),"dfcash.shape after groupby: ",dfcash.shape)
#print (lineno(),"兑付数量吨： ",dfcash['兑付升数'].sum()/1270)
#print (lineno(),"兑付金额万元： ",dfcash['兑付金额'].sum()/10000)
#主表中更新兑付数量和兑付金额
dfall=pd.merge(df,dfcash,how='left',on=['卡号(card_bn)'])
print ("dfall.shape after merge: ",dfall.shape)
dfall=dfall.fillna(value=0)
print (lineno(),"销售数量吨： ",(df['卡升数(card_litre)'].sum()+df['赠送升数(give_litre)'].sum())/1270)
#print (lineno(),"销售数量吨： ",dfall['销售合计升数'].sum()/1270)
print (lineno(),"兑付数量吨： ",dfall['兑付升数'].sum()/1270)


#加载单价表格
os.chdir(r"D:\workspace")
dfprice = pd.read_excel('price.xlsx',header=0,index_col=None,na_values=['NA'])
#dfprice = pd.read_csv('price.csv',header=0,index_col=None,na_values=['NA'])
#合并
dfall=pd.merge(dfall,dfprice,how='left', on=None,left_on=['地区名称(region_name)','油品名称(oil_name)'],right_on=['城市', '油品类型'])
print (lineno(),"dfall.shape after merge price: ",dfall.shape)
print (lineno(),"销售数量吨： ",(df['卡升数(card_litre)'].sum()+df['赠送升数(give_litre)'].sum())/1270)
print (lineno(),"兑付数量吨： ",dfall['兑付升数'].sum()/1270)
dfall=dfall.fillna(value=0)


#主体的计算
dfall['剩余升数']=dfall['卡升数(card_litre)']+dfall['赠送升数(give_litre)']-dfall['兑付升数']
#使用兑付金额的统计列，针对新的储油卡，在购买单价低于兑付单价时，公司亏损，购买单价高于兑付单价时，实现盈亏为0；

dfall['已经实现盈亏']=dfall['兑付升数']*dfall['购买单价(buy_price)']-dfall['兑付金额']-dfall['赠送升数(give_litre)']*dfall['购买单价(buy_price)']
dfall['浮动盈亏']=-dfall['剩余升数']*(dfall['当前单价']-dfall['购买单价(buy_price)'])
dfall['固定成本']=0

#针对新储油卡的实现盈亏，没有兑付为正数时，更改为0
print (lineno(),df[df['卡类型(card_type)']=='大众储油卡(新)'].shape)
dfall.loc[(dfall['卡类型(card_type)']=='大众储油卡(新)') & (dfall['已经实现盈亏']>0),'已经实现盈亏']=0

#针对新储油卡的浮动盈亏，为正数时，更改为0
print (lineno(),df[df['卡类型(card_type)']=='大众储油卡(新)'].shape)
dfall.loc[(dfall['卡类型(card_type)']=='大众储油卡(新)') & (dfall['浮动盈亏']>0),'浮动盈亏']=0
#dfall[dfall['卡类型(card_type)']=='大众储油卡(新)']['浮动盈亏']=0
#dfall[dfall['浮动盈亏']>0]['浮动盈亏']=0

#浮动盈亏小于0时，要乘以比例
ratio=pd.DataFrame([0.2,0.25,0.3,0.35],index=[100,200,400,800],columns=['ratio'])
dfall=pd.merge(dfall,ratio,how='left', on=None,left_on=['卡升数(card_litre)'],right_index=True)
#ratio={100:0.2,200:0.25,400:0.3,800:0.35}
#dfall['ratio']=dfall[(dfall['卡类型(card_type)']=='大众储油卡(新)') & (dfall['浮动盈亏']<0)]['卡升数(card_litre)'].map(ratio)
dfall.loc[(dfall['卡类型(card_type)']=='大众储油卡(新)') & (dfall['浮动盈亏']<0),'浮动盈亏']=dfall['浮动盈亏']*dfall['ratio']
#dfall.loc[(dfall['卡类型(card_type)']=='大众储油卡(新)'),:]
#df2.loc[(df2['卡类型(card_type)']=='大众储油卡(新)'),'总盈亏'].sum()

#固定成本的计算
fixratio=pd.DataFrame([0.01125,0.0275,0.04875,0.075],index=[100,200,400,800],columns=['fixratio'])
dfall=pd.merge(dfall,fixratio,how='left', on=None,left_on=['卡升数(card_litre)'],right_index=True)
dfall.loc[dfall['卡类型(card_type)']=='大众储油卡(新)','固定成本']=-dfall['购买金额(payout)']*dfall['fixratio']


dfall['总盈亏']=dfall['已经实现盈亏']+dfall['浮动盈亏']+dfall['固定成本']
print(lineno(),"total PL in ten thousand:",round(dfall['总盈亏'].sum()/10000,2))
dfall.drop(['卡号(card_bn)','当前日期','城市','油品类型'],axis=1,inplace=True)


df1=dfall.copy(deep=True)
os.chdir(r"D:\workspace")
df1.loc[df1['卡类型(card_type)']=='大众储油卡(新)',['生成时间(create_time)','卡类型(card_type)', '地区名称(region_name)', '油品名称(oil_name)',\
       '购买单价(buy_price)', '购买金额(payout)', '卡升数(card_litre)','兑付升数','兑付金额',\
       '剩余升数','当前单价']].to_csv("new.csv",index=False)
df1.loc[df1['卡类型(card_type)']=='大众储油卡(新)',:].to_excel("new2.xlsx",index=False)


dfall=dfall.groupby(['生成时间(create_time)','卡类型(card_type)', '地区名称(region_name)', '油品名称(oil_name)'])['购买金额(payout)','卡升数(card_litre)','赠送升数(give_litre)','兑付升数','兑付金额','剩余升数','已经实现盈亏','浮动盈亏','总盈亏'].sum().reset_index()
dfall=dfall.sort_values(['生成时间(create_time)','卡类型(card_type)', '地区名称(region_name)', '油品名称(oil_name)'])
#print (dfall.describe())
print(lineno(),"已经实现盈亏:",round(dfall['已经实现盈亏'].sum()/10000,2))
print(lineno(),"浮动盈亏:",round(dfall['浮动盈亏'].sum()/10000,2))
print(lineno(),"Exposure in tons:",round(dfall['剩余升数'].sum()/1270,2))
print(lineno(),"total PL in ten thousand:",round(dfall['总盈亏'].sum()/10000,2))


os.chdir(r"D:\workspace\history")
#dfall.to_excel('PL.xlsx',index=False)
file = "PL"+str(time.strftime("%Y-%m-%d", time.localtime())) + ".xlsx"
dfall.to_excel(file,index=False)

'''
table = pd.DataFrame.pivot_table(dfall, values=['购买金额(payout)','卡升数(card_litre)','赠送升数(give_litre)','兑付升数', '兑付金额'], index=['生成时间(create_time)', '卡类型(card_type)', '地区名称(region_name)', '油品名称(oil_name)'],columns=[], aggfunc=sum)
table=table.reset_index().fillna(value=0)
'''

end=time.clock()
print ("Running duration: %f s" % (end-start))












