# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 09:23:56 2017

@author: wangxj
"""
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
    
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
        
def my_function():
    """
    Do nothing, but document it.
    
    No, really, it doesn't do anything.
    """
    pass

def f(ham: str, eggs: str = 'eggs') -> str:
   print("Annotations:", f.__annotations__)
   print("Arguments:", ham, eggs)
   return ham + ' and ' + eggs


for x in range(1, 11):
   print(str(x).rjust(2), repr(x*x).rjust(3), end=' ')
   # Note use of 'end' on previous line
   print(repr(x*x*x).rjust(4))
   
   
   
   
   
   
   
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    except BaseException:
        print("BaseException")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
   
   

   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   