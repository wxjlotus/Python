# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 17:42:02 2017

@author: wangxj


我们知道print也可输出到文件。
在IDLE中输入

    f = open('text.txt', 'w')
    print('ABC',  file = f)



可以看到text.txt文件这时还是为空，只有f.close()后才将内容写进文件中。
如果改为

    print('ABC', file = f, flush = True)



则不用close文件立即就能看到文件有内容了。
"""
f = open('text.txt', 'a')
print ('-'*20,file = f)
print('ABC',  file = f)

from datetime import datetime
now = datetime.now() # 获取当前datetime
print("now by for:",now,file = f)
#制定日期和时间
dt = datetime(2017, 5, 27, 17, 15) # 用指定日期时间创建datetime
print("fixed date:",dt,file = f)
f.close()


with open('text.txt', 'a') as f:
	print("now by with:",now,file = f)
