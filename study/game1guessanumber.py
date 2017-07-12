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
limit=10
#num=int(input("guess a number:"))
constant=np.random.randint(0,limit)
loop=0
while True:
    try:
        print("*"*23)
        print("range[0,%d)" %(limit),end=' ')
        num=int(input("Input a number:"))
    except ValueError as e:
        print('ValueError:', e)
        continue
    loop+=1
    if num==constant:
        print("Congratulations,you are right!")
        print ("You tried",loop,"times.")
        break        
    elif num>constant:
        print(num,"is too large")
    else: print (num, "is too small")
    

end=time.clock()
print ("Running duration: %f s" % (end-start))



