# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 11:40:10 2017

@author: wangxj


import pandas as pd
df = pd.DataFrame({'a': [1, 2, 3], 'b': ['a', 'b', 'c'],'c': ["A","B","C"]})

print(df.loc[1,:])
print(df.iloc[1,:])
print(df.iloc[:,1])
print(df.iloc[1,:])
print(df.iloc[1:2,:])
print(df.iloc[::-1,:])
print(df.iloc[0:2:2,:])
"""
import time
import pandas as pd
import numpy as np
import re
start =time.clock()
#改变活动目录，r代表转义字符不生效
import sys
def lineno():
    try:raise Exception
    except:f = sys.exc_info()[2].tb_frame.f_back
    return f.f_lineno
print ("line num: ",lineno())

'''
#python内置字符串处理
a = 'a,b, guide'
print(lineno(),a.split(','))
print(lineno(),[x.strip() for x in a.split(',')])
first,second,third = [x.strip() for x in a.split(',')]
print(lineno(),first)
print(lineno(),second)
print(lineno(),third)
print(lineno(),first + third)
print(lineno(),first.join(third))
print(lineno(),''.join([third,first]))
print(lineno(),'a' in a)
print(lineno(),a.find(':'))
#print(lineno(),a.index(':'))
print(lineno(),a.count(','))






#正则表达式
text = 'foo    bar\t baz  \tqux'
print(lineno(),re.split('\s+', text)) # \s+  表示一个或多个空格
regex = re.compile('\s+')  # 创建regex对象，多次复用，减少大量CPU时间
print(lineno(),regex.split(text))
print(lineno(),regex.findall(text))  # 所有text中匹配到的对象

# match ：从头开始匹配
# search：第一个
# findall：找到所有


'''


text='''
Dave dave@google.com
Steve steve@gmail.com
Rob rob@gmail.com
Ryan ryan@yahoo.com
Carl carl@live.com
Peter peter@gmail.com
Rob rob@google.com
Lisa lisa@yahoo.com
Shawn wxjlotus@126.com
'''

'''
pattern=r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'
regex=re.compile(pattern,flags=re.IGNORECASE)
print (lineno(),regex.findall(text))

print(lineno(),regex.search(text))
print(lineno(),regex.search(text).group(0))


print(lineno(),regex.sub('HAHAHA', text))
print(lineno(),regex.sub("", text))


# 分组
pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'

regex = re.compile(pattern, flags=re.IGNORECASE)

m=regex.match('wesm@bright.net')

print (lineno(),m.groups())
print (lineno(),m.group(0))
print (lineno(),m.group(1))
print (lineno(),m.group(2))
print (lineno(),m.group(3))


# 返回一个大的列表
print (lineno(),regex.findall(text))

'''
#pandas矢量化字符串操作函数
data = {'Dave':'dave@google.com','Dave1':'dave@google.com','Dave':'dave@google.com','Steve':'steve@gmail.com','Rob':'rob@gmail.com','Ryan':'ryan@yahoo.com','Wes':np.nan}

data = pd.Series(data)

#data=data.str.replace('\S+/','').str.replace(':\S+','')

'''
print(lineno(),data.isnull())
# 查看是否包含，返回一个bool Series


print(lineno(),data.str.contains('gmail'))
pattern=r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'
# 返回一个匹配好的Series
print(lineno(),data.str.findall(pattern, flags=re.IGNORECASE))
matches = data.str.match(pattern, flags=re.IGNORECASE)
print(lineno(),matches)
print(lineno(),matches.str.get(1))
print(lineno(),matches.str.get(2))
print(lineno(),matches.str[0])
print(lineno(),data.str[:5])







s=pd.Series(['a1','A2','b1','ab2','c3','abd','a2c',np.nan,'a1b'])
print ('\ns')
print (s)
pattern=r'[a-z][0-9]'
print ('\ncontains')
print (s.str.contains(pattern))
print ('\nselect data')
print (s[s.str.contains(pattern,na=False)])
print ('\nmatch')
print (s.str.match(pattern,as_indexer=False))
print ('\nstartwith')
#print (s.str.startwith('a',na=False))
print (s[s.str.contains('^a',na=False)])
print ('\nend with')
#print (s[s.str.endwith('1',na=False)])
print (s[s.str.contains('1$',na=False)])
'''

end=time.clock()
print ("Running duration: %f s" % (end-start))








