#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
#=============================================================================
#  FileName:        xf.py
#  Description:     获取当前位置的行号和函数名
#  Version:         1.0
#=============================================================================
'''
import sys
def get_cur_info():
    """Return the frame object for the caller's stack frame."""
    try:
        raise Exception
    except:
        f = sys.exc_info()[2].tb_frame.f_back
    return (f.f_code.co_name, f.f_lineno)

def callfunc():
    print ("line num: ",get_cur_info())

 
if __name__ == '__main__':
    callfunc()
    
