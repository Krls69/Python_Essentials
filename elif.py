# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 19:20:53 2022

@author: KRLOS RE
"""

acl=int(input("Ingrese el # de ACL "))
if acl>=1 and acl<=99:
    print("La ACL es estandar")
elif acl>=100 and acl<=199:   
    print("La ACL es extendida")
elif acl>=200 and acl<=299:   
    print("La ACL es mas extendida ")    
else:
    print("El dato ingresado no es de un ACL")    

