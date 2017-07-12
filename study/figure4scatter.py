# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 13:56:55 2017

@author: wangxj
"""

import numpy as np
import matplotlib.pyplot as plt

fig,ax=plt.subplots()
ax.plot(10*np.random.randn(100),10*np.random.randn(100),'ro')
ax.set_title('Simple Scattter')


plt.show()