# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 14:38:27 2016

@author: wangxj
"""

import os,sys,string
import poplib
import email
from email import parser
#设置邮箱服务器、邮箱账号密码信息
host='oa.bwoil.com'#设置邮箱服务器
username='wangxj'#设置邮箱账号
password='oa123456'#设置邮箱密码
#连接服务器并登陆
popConn=poplib.POP3(host) #连接服务器
print popConn.getwelcome()#获取服务器欢迎信息，测试用，可删除
popConn.user(username)#输入账号
popConn.pass_(password)#输入密码
#获取邮箱相关信息
emailInf=popConn.stat()#返回邮箱的邮件信息（邮件个数、邮件总大小）
emailListInf=popConn.list()#返回邮件列表（响应，每个邮件的索引及大小，字节数）
print emailListInf[1]#输出邮件列表信息，测试用，可删除
print len(emailListInf[1])#输出邮件个数，测试用，可删除
ranges=range(1,len(emailListInf[1])+1)#设置邮件索引，用于多个邮件读取
messages=popConn.retr(len(emailListInf[1]))#获取最新邮件的内容（响应，内容，字节数）

#若想读取其他邮件，修改retr的参数值
messages="\n".join(messages[1])#将邮件内容用换行符连接
print messages#测试用，可删除
print '====================' 
msg=parser.Parser().parsestr(messages)#解析邮件内容
print msg#测试用，可删除
#设置文件保存路径
savePath='D: /'#设置保存路径
if not os.path.exists(savePath): 
   os.makedirs(savePath)
####解析邮件头，并信息写入相应log日志中
mailName=msg.get('Subject') 
h = email.Header.Header(mailName) 
dh = email.Header.decode_header(h) 
mailName = dh[0][0] 
mailInf=open(savePath+mailName+'.log','w') 
print >> mailInf,"Date:",msg.get('Date'),'\n' 
print >> mailInf,"From:",msg.get('From'),'\n' 
print >> mailInf,"To:",msg.get('To'),'\n' 
print >> mailInf,"Subject:",mailName,'\n' 
print >> mailInf,"Data:"
#解析邮件体,并下载附件、将正文内容写入log日志中
for part in msg.walk(): 
   fileName=part.get_filename()#返回每个part的附件名字，如果没有附件，返回空
   h = email.Header.Header(fileName) 
   dh = email.Header.decode_header(h) 
   fileName = dh[0][0] 
   print fileName 
   if fileName:#有附件并下载附件内容（下载方式为在本地新建文件并将附件内容写入该新建文件）
       fileName=savePath+fileName 
       fileData=part.get_payload(decode=True)#获取附件内容
       fileName="%s" %(fileName)#设置新建文件名
       f=open(fileName,'wb')#打开新建文件
       f.write(fileData)#将附件内容写入新建文件
       f.close()#关闭新建文件
contentType=part.get_content_type()#返回正文内容类型
if contentType=='text/plain'or contentType=='text/html': 
   contentData=part.get_payload(decode=True)#获取邮件正文内容
   print >> mailInf,contentData#将正文内容写入log日志中
mailInf.close() 
