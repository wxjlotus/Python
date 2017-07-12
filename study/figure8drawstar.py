# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 16:38:27 2017

@author: wangxj
"""


# drawstar.py

from turtle import Turtle
p = Turtle()
p.speed(3)
p.pensize(5)
p.right(20)
p.color("green","yellow")
#p.fillcolor("red")
p.begin_fill()
for i in range(5):
    p.forward(200)
    p.right(144)
p.end_fill
