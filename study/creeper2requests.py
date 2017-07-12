# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 10:35:58 2017

@author: wangxj
"""

import requests
import time


from bs4 import BeautifulSoup

r=requests.get("http://python123.io/ws/demo.html")
#print(r.text)
demo=r.text
soup=BeautifulSoup(demo,'html.parser')
print(soup.prettify)
print(soup.title)








#搜索示例

#url = 'http://www.baidu.com/s'
#try:
#    kv={'wd':'python'}
#    r = requests.get(url,params=kv)
#    r.raise_for_status()
#    print(r.status_code)
##    print('-'*30)
##    r.encoding = r.apparent_encoding
##    print(r.headers)
##    print('-'*30)
#    print(r.request.headers)
#    print(r.request.url)
#    print(len(r.text))
##    print(r.text[0:20])
#except:
#    print("Exception")



#爬虫示例
#url = 'http://www.baidu.com'
#try:
#    kv={'user-agent':'Mozilla/5.0'}
#    r = requests.get(url,timeout=5,headers=kv)
#    r.raise_for_status()
#    print(r.status_code)
#    print('-'*30)
#    r.encoding = r.apparent_encoding
#    print(r.headers)
#    print('-'*30)
#    print(r.request.headers)
#    print('-'*30)
#    print(r.text[0:20])
#except:
#    print("Exception")








#    getHTMLText(url)
#import requests
#r=requests.get("http://www.baidu.com")
#print(r.status_code)
#print(r.text)
#print(r.apparent_encoding)
#print(r.encoding)
#r.encoding='utf-8'
#print(r.encoding)
#print(r.text)


#def getHTMLText(url):
#    try:
#        r = requests.get(url,timeout=30)
#        r.raise_for_status()
#        r.encoding = r.apparent_encoding
#        print(r.headers)
#        print(r.request.headers)
#        return r.text
#    except:
#        return "产生异常"
#def atime():
#    statr = time.time()
#    url = 'http://www.baidu.com'
#    for i in range(100):
#        getHTMLText(url)
#    end = time.time()
#    return end - statr
#
#if __name__ == "__main__":
#    url = 'http://www.baidu.com'
#    print(getHTMLText(url))
#    getHTMLText(url)



#import requests
#import time
#
#def getHTMLText(url):
#    try:
#        r = requests.get(url)
#        r.raise_for_status()
#        r.encoding = r.apparent_encoding
#        return r.text
#    except:
#        return ''
#
#def main():
#    start = time.time()
#    for i in range(100):
#        getHTMLText('http://www.pku.edu.cn/')
#        print(i)
#    stop = time.time()
#
#    print('爬取时间为：{:.3f}s'.format(stop - start))

#main()