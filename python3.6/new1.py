# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 13:53:30 2017

@author: Thinkpad
"""

import numpy as np
import pandas as pd

dates=pd.date_range('20170617',periods=6)
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
#print (df)


val='abadd c,d'
print(val)
val.split(',')
arr=val.strip()
arr=[x.strip() for x in val.split(',')]

s = pd.Series(['a_b_c', 'c_d_e', np.nan,'f_g_h'])
s.str.replace("_", ".")
