#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#计算程序运行时间
import time
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
start =time.clock()
#打印行号
def lineno():
    try:raise Exception
    except:f = sys.exc_info()[2].tb_frame.f_back
    return f.f_lineno
print ("line num: ",lineno())

'''
#测试颜色、风格、标记控制
a=np.arange(10)
#plt.plot(a,a*1.5,'gs:')
plt.plot(a,a*1.5,'go-',a,a*2.5,'rx-.',a,a*3.5,'*',a,a*4.5,'b-.')
plt.show
'''
#matplotlib.rcParams['font.family']='STSong'
#matplotlib.rcParams['font.size']=20
a=np.arange(0.0,5.0,0.02)
plt.plot(a,np.cos(2*np.pi*a),'r--')
plt.xlabel('横轴：时间',fontproperties='SimHei',fontsize=15)
plt.ylabel('纵轴：波幅',fontproperties='SimHei',fontsize=15)
plt.title(r'正弦波实例,$y=cos(2\pi x)$',fontproperties='SimHei',fontsize=25)
plt.annotate(r'$\mu=100$',xy=(2,1),xytext=(3,1.5),arrowprops=dict(facecolor='black',shrink=0.1,width=2))
plt.axis([-1,6,-2,2])
plt.grid(True)
plt.show                   

                   






end=time.clock()
print ("Running duration: %f s" % (end-start))



