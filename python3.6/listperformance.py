# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 16:41:22 2017

@author: wangxj
"""

from matplotlib import pyplot
import pylab

size = 200
axis_x = [i for i in xrange(size)]
axis_y = []
for i in xrange(size):
    axis_y.append(axis_y.__sizeof__())

pyplot.title("The size of list.")
pyplot.xlabel("Number of objects in the list.")
pyplot.ylabel("List size")
pyplot.plot(axis_x, axis_y, color = "red")
pylab.show()

