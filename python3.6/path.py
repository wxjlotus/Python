# -*- coding: utf-8 -*-
"""
Created on Thu May 25 13:50:38 2017

@author: wangxj
"""


import random

x = random.choice(range(100))
y = random.choice(range(200))
if x > y:
    print('x:',x)
elif x == y:
    print('x+y', x + y)
else:
    print('y:',y)
    
#程序安装路径，官方文档有介绍
import sys
path = sys.executable
print (path)
folder=path[0:path.rfind(os.sep)]
print (folder)