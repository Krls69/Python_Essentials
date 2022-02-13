milla=1.609344
galon=3.785411784

def l100kmtompg(liters):
    conver=1/liters*100*galon/milla
    print("La conversion de ", liters,"1/100km a MPG es: ",conver,"MPG")

def mpgtol100km(miles):
    conver2=1/miles*galon*100/milla
    print("La conversion de ", miles,"MPG a 1/100km es: ",conver2,"l/100km")

eleccion=int(input("Ingrese 1 para convertir l/100km a MPG o 2 para convertir MPG a 1/100km: "))

if eleccion==1:
    a=float(input("Ingrese el valor en l/100km: "))
    l100kmtompg(a)
elif eleccion==2:
    a=float(input("Ingrese el valor en MPG: "))
    mpgtol100km(a)


    

             
