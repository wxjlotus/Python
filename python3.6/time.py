#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#计算程序运行时间
import time
start =time.clock()
print("start")
'''
#!/usr/bin/python3
# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 10000:
    print(b, end=' ')
    a, b = b, a+b
    

print('两数之和为 %.1f' %(float(input('输入第一个数字：'))+float(input('输入第二个数字：'))))
'''
ticks = time.time()
print ("当前时间戳为:%0.3f" % ticks)



localtime = time.localtime(time.time())
print ("本地时间为 :", localtime)
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print (time.strftime("%Y-%m-%d", time.localtime()))
t = (2016, 2, 17, 17, 3, 38, 1, 48, 0)
secs = time.mktime( t )
print ("time.mktime(t) : %f" %  secs)
print ("asctime(localtime(secs)): %s" % time.asctime(time.localtime(secs)))
time.sleep(0.1)
print("end")
end=time.clock()
print ('\n',"Running duration: %f s" % (end-start))












