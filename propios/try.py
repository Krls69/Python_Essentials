# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 18:12:49 2022

@author: KRLOS RE
"""

try:
    x = int (input("Enter a number: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")
print("THE END.")