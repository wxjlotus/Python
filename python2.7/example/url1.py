# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 09:01:12 2016

@author: wangxj
"""
from smtplib import SMTP as smtp
s = smtp('smtp.python.is.cool')
s.set_debuglevel(1)
s.sendmail('wangxj@bwoil.com', ('wesley@python.is.cool',
'chun@python.is.cool'), ''' From: wesley@python.is.cool\r\nTo:
wesley@python.is.cool, chun@python.is.cool\r\nSubject: test
msg\r\n\r\nxxx\r\n.''')
