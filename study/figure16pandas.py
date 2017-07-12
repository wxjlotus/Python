#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#计算程序运行时间
import time
start =time.clock()
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')
#打印行号

def lineno():
    try:raise Exception
    except:f = sys.exc_info()[2].tb_frame.f_back
    return f.f_lineno
print ("line num: ",lineno())

#ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2016', periods=1000))
#ts = ts.cumsum()
#ts.plot()
#
#df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))
#df = df.cumsum()
#plt.figure()
#df.plot()
#
#df3 = pd.DataFrame(np.random.randn(1000, 2), columns=['B', 'C']).cumsum()
#df3.plot(x='A', y='B')
#
#plt.figure();
#df.iloc[5].plot(kind='bar')


#df2 = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
#df2.plot.bar()
#df2.plot.bar(stacked=True)
#df2.plot.barh(stacked=True);


#df4 = pd.DataFrame({'a': np.random.randn(1000) + 1, 'b': np.random.randn(1000),'c': np.random.randn(1000) - 1}, columns=['a', 'b', 'c'])
#plt.figure();
#df4.plot.hist(alpha=0.5)
#plt.figure();
#df4.plot.hist(stacked=True, bins=20)
#
#
#
#
#df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
#df.plot.box()



#
#df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
#df.plot.scatter(x='a', y='b')
#ax = df.plot.scatter(x='a', y='b', color='DarkBlue', label='Group 1');
#df.plot.scatter(x='c', y='d', color='DarkGreen', label='Group 2', ax=ax);
#df.plot.scatter(x='a', y='b', c='c', s=50);
#df.plot.scatter(x='a', y='b', s=df['c']*200);


series = pd.Series(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], name='series')
series.plot.pie(figsize=(6, 6))


#normals = pd.Series(10*np.random.normal(size=10))
#normals.plot()
#normals.cumsum().plot(grid=False)
#
#
#
#
#df1 = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
#df1['num']=np.arange(0,50)
#df1.plot.scatter(x='num', y='b');
#df1.plot.scatter(x='a', y='b');







#end=time.clock()
#print ("Running duration: %f s" % (end-start))
#time.sleep(3)
end=time.clock()
print ("Running duration: %f s" % (end-start))



