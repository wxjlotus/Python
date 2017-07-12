#!/usr/bin/env python
# -*- coding:utf-8 -*-
#计算程序运行时间
import time
import pandas as pd
import os
start =time.clock()
#改变活动目录，r代表转义字符不生效
#需要提前删除单引号
os.chdir(r"D:\workspace\saleoffline") 
#print os.getcwd()
#获取目录下所有csv文件，并打印数量；
filenames = [x for x in os.listdir(os.getcwd()) if x.endswith('xls')]
print "the number of files: ",len(filenames)
#创建空DataFrame，并罗列汇总所有记录
df=pd.DataFrame()
#num=0
for file in filenames:
    dftemp = pd.read_excel(file,sheetname=0, header=0, skiprows=4)
    #print file,"  ",dftemp.shape
    #print dftemp.columns[:3]
    #num=dftemp.index.size+num
    df=pd.concat([dftemp,df])
#print num
    
print "df.shape: ",df.shape
df=df[df[u'业务日期']>'2016-1-1']
df=df.drop([u'销售均价（元/吨）'],axis=1)
print "df.shape after filter: ",df.shape
df[u'业务日期']=pd.to_datetime(df[u'业务日期'])
df[u'业务日期']=df[u'业务日期'].dt.strftime('%Y-%m-%d')
df=df.sort_values(by=[u'业务日期',u'订单编号'])
#df[u'业务日期'].dt.year
#df[u'业务日期'].dt.strftime('%Y-%m-%d')



os.chdir(r"D:\workspace") 
df.to_excel('saleoffline.xls', sheet_name='Sheet1', header=True, index=False, startrow=0, startcol=0)


end=time.clock()
print "Running duration: %f s" % (end-start)





































'''


import time,datetime
# date to str
print time.strftime("%Y-%m-%d %X", time.localtime())
#str to date
t = time.strptime("2009 - 08 - 08", "%Y - %m - %d")
y,m,d = t[0:3]
print datetime.datetime(y,m,d)

print round(3,4)




s="你好"
s=s.decode('utf-8').encode('utf-8')
print s
print time.time()
print time.time()-86400
print time.strftime('%Y%m%d',time.localtime(time.time()))
print time.strftime('%Y%m%d',time.localtime(time.time()-86400))

print 24*60*60







import sys  
reload(sys)  
print sys.getdefaultencoding()
sys.setdefaultencoding('utf8')
print sys.getdefaultencoding()


import sys 
print 'default encoding: ' , sys.getdefaultencoding()
print 'file system encoding: ' , sys.getfilesystemencoding()
print 'stdout encoding: ' , sys.stdout.encoding
print u'u"中文" is unicode: ', isinstance(u'中文',unicode)
print u'"中文" is unicode: ', isinstance('中文',unicode)



def getCoding(strInput):

    #获取编码格式

    if isinstance(strInput, unicode):
        return "unicode"
    try:
        strInput.decode("utf8")
        return 'utf8'
    except:
        pass
    try:
        strInput.decode("gbk")
        return 'gbk'
    except:
        pass
        
def tran2UTF8(strInput):

    #转化为utf8格式

    strCodingFmt = getCoding(strInput)
    if strCodingFmt == "utf8":
        return strInput
    elif strCodingFmt == "unicode":
        return strInput.encode("utf8")
    elif strCodingFmt == "gbk":
        return strInput.decode("gbk").encode("utf8")

def tran2GBK(strInput):

    #转化为gbk格式

    strCodingFmt = getCoding(strInput)
    if strCodingFmt == "gbk":
        return strInput
    elif strCodingFmt == "unicode":
        return strInput.encode("gbk")
    elif strCodingFmt == "utf8":
        return strInput.decode("utf8").encode("gbk")



s="中文"
print getCoding(s)
print tran2UTF8(s)
print tran2GBK(s)





dfd= pd.read_csv(r"D:\workspace\sale\sale20161201-20161204.csv",header=0,index_col=None,na_values=['NA'])
dfd=dfd[['卡号(card_bn)','卡类型(card_type)','地区名称(region_name)','油品名称(oil_name)','购买单价(buy_price)','购买金额(payout)','卡升数(card_litre)', '赠送升数(give_litre)','生成时间(create_time)']]
#print "dfd.iloc[:,-1]:  ",dfd.iloc[:,-1].head(3)
#print pd.to_datetime(dfd.iloc[:,-1]).head(3)
#print "--"*90

for i in range(dfd.index.size):
    dfd.iat[i,-1]=time.strftime("%Y%m%d",time.strptime(dfd.iat[i,-1],'%Y-%m-%d %H:%M'))
print "dfd.iloc[:,-1]:  ",dfd.iloc[:,-1].head(3)
print dfd.index.size




dfd.drop_duplicates('生成时间(create_time)',keep='first',inplace=True)
print dfd.index.size
dfd.sort_values('生成时间(create_time)', axis=0, ascending=True, inplace=True)

dates = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])
print df.shape
#print df.iloc[:,[0,1]]
print df
df=df.applymap(lambda x: '%.2f' % x**2)
print df



freq=1
for i in range(len(df.index)):
    for j in range(len(df.columns)):
        #print df.index[i]
        #print df.columns[j]
        df.columns[j]
        print freq," ",i," ",j," ",df.iloc[i,j]
        df.iloc[i,j]=15156
        print freq," ",i," ",j," ",df.iloc[i,j]
        freq=freq+1
df.head(3)
print pd.to_datetime(dates)
'''
