# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 14:29:19 2017

@author: wangxj
"""

import pandas as pd

data = pd.DataFrame([[1, "2"], [3, "123456486465"]])
data.columns = ["one", "two"]

print(data)

# 当前类型
print("----\n修改前类型：")
print(data.dtypes)

# 类型转换
data[["two"]] = data[["two"]].astype(int)

# 修改后类型
print("----\n修改后类型")
print(data.dtypes)

# 类型转换
data[["two"]] = data[["two"]].astype(str)

# 修改后类型
print("----\n修改后类型")
print(data.dtypes)