#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
start =time.clock()

import xlrd
filename = 'D:\workspace\IF1606.xls'   
data = xlrd.open_workbook(filename,on_demand=True) 
#table = data.sheets()[0]          #通过索引顺序获取
#table = data.sheet_by_index(0) #通过索引顺序获取
#table = data.sheet_by_name(u'Sheet1')#通过名称获取
sheetname = data.sheet_names()
print sheetname

end=time.clock()
print "Running duration: %f s" % (end-start)

sheet = data.sheet_by_index(0) 
rows = sheet.nrows
cols = sheet.ncols
for i,row in enumerate(range(rows)):
    if i < 10 and i>3:
        value = sheet.row_values(row)
        print i,value
        
end=time.clock()
print "Running duration: %f s" % (end-start)