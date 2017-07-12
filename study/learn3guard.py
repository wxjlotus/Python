# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 14:17:58 2017

@author: wangxj
"""

def main():
    sum=0.0
    count=0
    xstr=input("Enter a number(<Enter> to quit)>>")
    while xstr!="":
        x=eval(xstr)
        sum=sum+x
        count=count+1
        xstr=input("Enter a number(<Enter> to quit)>> ")
    print ("\n The average of the numbers is %.2f" %(sum/count))
main()
    