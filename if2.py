# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 19:27:09 2022

@author: KRLOS RE
"""

firstname = input("Cual es su nombre: " )
lastname = input("Cual se su apellido: ")
location = input("Donde vive: ")
#age = input("Cual es su edad: ")
space = " "
print("Bienvenido al mundo python, se encuentra registrado con los siguientes datos: ")
#print("Nombre:",firstname,space,"Apellido:",lastname,space,"Ubicacion:",location,space,"Edad:",age)
print("Nombre:",firstname,space,"Apellido:",lastname,space,"Ubicacion:",location)

age = input("Cual es su edad: ")
age2=int(age)
if age2>=10 and age2<20:
    print("No esta registrado en base de datos")
elif age2>=21 and age2<30:
    print("No esta registrado en base de datos")
else:
    print("Esta registrado como")
    print("Nombre:",firstname,space,"Apellido:",lastname,space,"Ubicacion:",location,space,"Edad:",age)


