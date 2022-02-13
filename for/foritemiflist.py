# -*- coding: utf-8 -*-
"""
Created on Wed May  6 20:29:30 2020

@author: Juan Carlos
"""
switches=[]
devices=["R1","R2","R3",
         "S1","S2","S3",
         "S4","S5"]
for i in devices:
    if "S" in i:
        switches.append(i)
print (switches)