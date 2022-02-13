# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 19:03:01 2019

@author: CEC
"""

result = 0
n = 6
for i in range(1, n ,1):
    print(i)
    result += i
    #print(result)
    # this ^^ is the shorthand for
    #result = result + i
print("el resultado de la suma de 1 hasta n es:",
      result)