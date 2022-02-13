# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 19:22:56 2022

@author: KRLOS RE
"""

def direction(ciudad,calle,barrio):
    print("La direccion de envio es: ")
    print("Sector la: ",barrio)
    print("En la calle: ",calle)
    print("En la ciudad de: ", ciudad)
cl=input("Ingrese la calle: ")
ba=input("Ingrese el sector: ")
ci=input("Ingrese la ciudad: ")
direction(ci,cl,ba)
