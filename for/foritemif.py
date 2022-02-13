# -*- coding: utf-8 -*-
"""
Created on Wed May  6 20:29:30 2020

@author: Juan Carlos
"""
router=[]
switches=[]
devices=["R1","R2","R3","S1","S2","AP1"]
for a in devices:
    if "R" in a:
        router.append(a)
    else:
        switches.append(a)
print(switches)
print(router)        