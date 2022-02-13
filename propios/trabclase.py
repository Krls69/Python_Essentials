# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 18:08:19 2022

@author: KRLOS RE
"""

while True:
    x=input("Enter a number to count to: ")
    if x == 'q' or x == 'quit':
        break
    x=int(x)
    y=1
    while True:
        print(y)
        y+=1 #o tambien y=y+1
        if y>x:
            break