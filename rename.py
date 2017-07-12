# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 17:59:48 2017

@author: wangxj
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 13:34:10 2017

@author: wangxj
"""

#计算程序运行时间
import time
start =time.clock()
import re
import os
import shutil
import numpy as np
import pandas as pd
localtime = time.localtime(time.time())
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

import sys
def lineno():
    try:raise Exception
    except:f = sys.exc_info()[2].tb_frame.f_back
    return f.f_lineno
#print ("line num: ",lineno())

print(os.getcwd())
path=r"C:\Users\wangxj\Downloads"
os.chdir(path)
print(os.getcwd())
filenames = [x for x in os.listdir(os.getcwd()) if x.endswith('csv')]
print (lineno(),"filenames: ",len(filenames))
print(pd.Series(filenames))
for file in filenames:
    if file.startswith('sale'):
        shutil.move(file,"D:\\workspace\\sale\\"+file)
    elif file.startswith('cash'):
        shutil.move(file,"D:\\workspace\\cash\\"+file)
    elif file.startswith('order'):
        shutil.move(file,"D:\\workspace\\order\\"+file)

path=r"D:\workspace\Python"
os.chdir(path)


end=time.clock()
print ("Running duration: %f s" % (end-start))












