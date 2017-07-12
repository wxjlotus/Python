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



#print(os.getcwd())
#path=r"C:\Users\wangxj\Downloads"
#os.chdir(path)
#print(os.getcwd())
#filenames = [x for x in os.listdir(os.getcwd()) if x.endswith('csv')]
#print (lineno(),"filenames: ",len(filenames))
#print(pd.Series(filenames))

#for file in filenames:
#    if file.startswith('sale'):
#        shutil.move(file,"D:\\workspace\\sale"+file)
#    elif file.startswith('cash'):
#        shutil.move(file,"D:\\workspace\\cash"+file)
#    elif file.startswith('order'):
#        shutil.move(file,"D:\\workspace\\order"+file)




path=r"d:\workspace"
outfile = open(r'D:\filelist.txt', 'a')
for root,dirs,files in os.walk(path):
    for name in files:
        if name.endswith('py'):
#            print(os.path.join(root,name))
            print(os.path.join(root,name), sep=' ', end='\n', file=outfile, flush=False)
outfile.close()
#os.stat(path)



#print (lineno(),os.path.dirname(os.path.abspath(__file__)))
#print (os.path.basename(os.path.abspath(__file__)))
##print (os.path.split(__file__)[0])
#print (os.path.split(__file__)[-1])
#print (os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.basename(__file__))))
#print (os.path.abspath(__file__))


#print(os.linesep)#返回操作系统换行字符串，在交互界面可用；
#df=pd.DataFrame(np.arange(0,100))
#name="test.csv"
#df.to_csv(name,index=False)
##os.rename("test.csv","D:\modified.csv")  #correct!
##shutil.move(name,"D:\modified.csv") #correct!
#os.rename("test.csv","D:\\"+name)  #correct!
##shutil.move(name,"D:\\"+name) #correct!
#os.remove("D:\\"+name)




path=r"D:\workspace\Python"
os.chdir(path)

end=time.clock()
print ("Running duration: %f s" % (end-start))












