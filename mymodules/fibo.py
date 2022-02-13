# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 20:06:39 2022

@author: KRLOS RE
"""

def fibona(num):
    a=0
    b=1
    while a<=num:
        print(a,end=" ")
        a=b
        b=a+b
#fibona(50)
        