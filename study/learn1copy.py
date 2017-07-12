# -*- coding: utf-8 -*-
#计算程序运行时间
import time
import sys
import pandas as pd
import numpy as np
start =time.clock()
#打印行号
def lineno():
    try:raise Exception
    except:f = sys.exc_info()[2].tb_frame.f_back
    return f.f_lineno
print ("line num: ",lineno())

np.random.seed(24)
a=np.array([2,23,4],dtype=np.int)
df = pd.DataFrame({'A': np.linspace(1, 10, 10)})
df = pd.concat([df, pd.DataFrame(np.random.randn(10, 4), columns=list('BCDE'))],
               axis=1)
df.iloc[0, 2] = np.nan

       
df = pd.DataFrame({'A':range(5) })
df1=df.copy(deep=True)
print (lineno(),id(df))
print (lineno(),id(df1))
df.iloc[0,0]=11
print (lineno(),id(df))

df = pd.DataFrame({'A':range(12) })
print (lineno(),id(df))   
df = df.loc[0:8,:]
print (lineno(),id(df))  
df['test']='tsts'
print (lineno(),id(df)) 



end=time.clock()
print ("Running duration: %f s" % (end-start))





