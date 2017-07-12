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
os.chdir(r"D:\workspace\saleall")
#获取当前目录下所有csv文件，并打印数量；
filenames = [x for x in os.listdir(os.getcwd()) if x.endswith('csv')]
#创建空DataFrame，并罗列汇总所有记录
df=pd.DataFrame()
print ('--'*20)
for file in filenames:
    print (file)
    dftemp = pd.read_csv(file,header=0,index_col=None,na_values=['NA'])
#    dftemp=dftemp[dftemp['状态(card_status)']!='失效']
    dftemp=dftemp[['卡号(card_bn)','卡类型(card_type)','地区名称(region_name)','油品名称(oil_name)','购买单价(buy_price)','购买金额(payout)','赠送金额(give_amount)','卡升数(card_litre)', '赠送升数(give_litre)','生成时间(create_time)','每期兑付期限单位(limit_distribute_unit)','每期兑付期限时间(limit_distribute_time)','兑付期数(cash_deadline)','订单号']]
    #卡类型筛选
#    dftemp=dftemp[dftemp['卡类型(card_type)'].isin(["大众储油体验卡","大众储油卡","大众储油卡(新)","全国加油卡","大众储油节日卡"])]
#    dftemp=dftemp[dftemp['卡类型(card_type)'].isin(["大众储油体验卡","大众储油卡","大众储油卡(新)"])]
    #体验卡1元特权与油价无关，需要删除;促销价的油品名称需要更改；
#    dftemp=dftemp[dftemp['油品名称(oil_name)']!='1元特权']
    dftemp['卡号(card_bn)']=dftemp['卡号(card_bn)'].astype(str)
    dftemp['卡号(card_bn)']=dftemp['卡号(card_bn)'].str.replace('\'','')
    #dftemp['卡号(card_bn)']=dftemp['卡号(card_bn)'].astype(int)
    df=pd.concat([dftemp,df])
df['生成时间(create_time)']=pd.to_datetime(df['生成时间(create_time)'])
df['生成时间(create_time)']=df['生成时间(create_time)'].map(pd.Timestamp.date)
df['订单号']=df['订单号'].astype(str)
df['订单号']=df['订单号'].str.replace('\'','')
print (lineno(),"大众储油卡(新)销售数量：",df[df['卡类型(card_type)']=='大众储油卡(新)'].shape)
df.loc[df['油品名称(oil_name)'].isin(['促销95#0119','促销95#0129', '促销95#0208','促销95#0218','促销汽油95#']),'油品名称(oil_name)'] = 'Ⅴ汽油95#'
print (lineno(),"销售数量吨： ",round((df['卡升数(card_litre)'].sum()+df['赠送升数(give_litre)'].sum())/1270,2))
#卡号理论上是唯一的
df.drop_duplicates(inplace=True)
print (lineno(),"df.shape after drop_duplicates: ",df.shape)
print (lineno(),'--'*30)
#print(df['购买金额(payout)'].groupby(df['卡类型(card_type)']).sum()/10000)
#df=df[['卡号(card_bn)', '卡类型(card_type)', '购买金额(payout)','每期兑付期限单位(limit_distribute_unit)', '每期兑付期限时间(limit_distribute_time)','兑付期数(cash_deadline)', '订单号']]
print(df['赠送金额(give_amount)'].sum()/10000)
print((df['购买单价(buy_price)']*df['赠送升数(give_litre)']).sum()/10000)

#os.chdir(r"D:\workspace\order")
#filenames = [x for x in os.listdir(os.getcwd()) if x.endswith('csv')]
#dforder=pd.DataFrame()
#for file in filenames:
#    print ("file: ",file)
#    dftemp = pd.read_csv(file,header=0,index_col=None,na_values=['NA'])
##    dftemp=dftemp[dftemp['商品名称(name)'].isin(["大众储油体验卡","大众储油卡","大众储油卡(新)","全国加油卡","大众储油节日卡"])]
##    print ("dftemp.shape: ",dftemp.shape)
#    dftemp=dftemp[['订单号(order_id)','订单状态(status)','商品名称(name)','订单总额(final_amount)','订单实付金额(payed)','订单折扣优惠(discount)','订单现金券减免(cpns_money)','订单油箱抵用金额(goil_money)']]
#    dforder=pd.concat([dftemp,dforder])
#dforder=dforder[dforder['订单状态(status)']!='已作废']
#dforder.drop_duplicates(inplace=True)
#print ("dforder.shape after concat: ",dforder.shape)
#print ("所有产品（理财+实体）：\n",dforder[['订单总额(final_amount)', '订单实付金额(payed)','订单折扣优惠(discount)','订单现金券减免(cpns_money)','订单油箱抵用金额(goil_money)']].sum()/10000)
#dforder['订单号(order_id)']=dforder['订单号(order_id)'].astype(str)
#dforder['订单号(order_id)']=dforder['订单号(order_id)'].str.replace('\'','')



#import sys
#print (sys.getsizeof(df)/1024/1024)
#os.chdir(r"D:\workspace")
#df.to_excel("saleall.xlsx")
#table=pd.pivot_table(df,values=['购买金额(payout)'],index=['订单号'],columns=['每期兑付期限单位(limit_distribute_unit)'],aggfunc=sum)
#dfall=pd.merge(dforder,df,how='left', on=None,left_on=['订单号(order_id)'],right_on=['订单号'])
#dfall=dfall.fillna(value=0)
#dfall.loc[dfall['卡类型(card_type)']==0,'卡类型(card_type)']='未知'
#dfall[['订单总额(final_amount)','订单实付金额(payed)', '订单折扣优惠(discount)', '订单现金券减免(cpns_money)','订单油箱抵用金额(goil_money)',]].groupby(['卡类型(card_type)','兑付期数(cash_deadline)','每期兑付期限时间(limit_distribute_time)','每期兑付期限单位(limit_distribute_unit)']).sum()
#dft=dfall.groupby(['卡类型(card_type)']).sum()/10000
#dft.to_excel("dft.xlsx")


#print(df['收益（元）(profit)'].sum()/10000) 收益变动的，含有固定成本和油价成本；
#print (lineno(),df['购买金额(payout)'].sum()/10000)
#print (lineno(),df['购买成本(cost)'].sum()/10000)
#print (lineno(),df['购买金额(payout)'].sum()/10000-df['购买成本(cost)'].sum()/10000)


#os.chdir(r"D:\workspace")
#df.to_csv('salesimple20160105-20170710.csv',index=False)


##section 2:加载兑付表格,计算兑付情况；
#os.chdir(r"D:\workspace\cash")
##获取目录下所有csv文件；
#filenames = [x for x in os.listdir(os.getcwd()) if x.endswith('csv')]
##创建空DataFrame，并罗列汇总所有记录
#dfcash=pd.DataFrame()
#for file in filenames:
#    dftemp = pd.read_csv(file,header=0,index_col=None,na_values=['NA'])
#    dftemp=dftemp[['产品名称(product_name)','储油通卡号(card_bn)', '交易类型(trade_type)', '数量(trade_nums)', '金额(income)','交易成功时间(trade_end_time)']]
#    dftemp=dftemp[dftemp['产品名称(product_name)'].isin(["大众储油体验卡","大众储油卡","大众储油卡(新)"])]
#    dftemp=dftemp[dftemp["交易类型(trade_type)"]=='兑付']
#    dftemp['储油通卡号(card_bn)']=dftemp['储油通卡号(card_bn)'].astype(str)
#    dftemp['储油通卡号(card_bn)']=dftemp['储油通卡号(card_bn)'].str.replace('\'','')
#    dfcash=pd.concat([dftemp,dfcash])
#print (lineno(),"dfcash.shape after contact:",dfcash.shape)
#print (lineno()," 兑付金额万元： ",dfcash['金额(income)'].sum()/10000)
#print (lineno()," 兑付数量吨： ",dfcash['数量(trade_nums)'].sum()/1270)
##变更为日期类型
#dfcash['交易成功时间(trade_end_time)']=pd.to_datetime(dfcash['交易成功时间(trade_end_time)'])
#dfcash['交易成功时间(trade_end_time)']=dfcash['交易成功时间(trade_end_time)'].map(pd.Timestamp.date)
##选择有效列
#dfcash=dfcash[['储油通卡号(card_bn)', '交易类型(trade_type)', '数量(trade_nums)', '金额(income)']]
#dfcash.columns=['卡号(card_bn)', '交易方向', '兑付升数','兑付金额']
##按照卡号汇总
#dfcash=dfcash.groupby(['卡号(card_bn)'])['兑付升数','兑付金额'].sum().reset_index()
##主表中更新兑付数量和兑付金额
#dfall=pd.merge(df,dfcash,how='left',on=['卡号(card_bn)'])
#print ("dfall.shape after merge: ",dfall.shape)
#dfall=dfall.fillna(value=0)
#print (lineno(),"销售数量吨： ",(df['卡升数(card_litre)'].sum()+df['赠送升数(give_litre)'].sum())/1270)
#print (lineno(),"兑付数量吨： ",dfall['兑付升数'].sum()/1270)



end=time.clock()
print ("Running duration: %f s" % (end-start))












