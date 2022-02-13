#If-elif-else
name=input("Ingrese ESPATIFILIO o espatifilo: ")
if name=="ESPATIFILIO":
    print('"Si, ¡El ESPATIFILIO ! es la mejor planta de todos los tiempos!"')
elif name=="espatifilo":
    print('"No, ¡quiero un gran ESPATIFILIO!"')
else:
    print('"¡ESPATIFILIO!, ¡No ' + name +'!"')

print()
income = float(input("Introduce el ingreso anual:"))
ingreso=85528.0
#
if income<ingreso:
    tax=income*18/100-556.2
    if tax<=0:
        tax=-income*0
else:
    tax=14839.2+(income-ingreso)*32/100

#
tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")
print()

year = int(input("Introduce un año:"))

#
if year>=1582:
    if year%4!=0:
        print("Año " +str(year) +" comun")
    elif year%100!=0:
        print("Año " +str(year) +" bisiesto")
    elif year%400!=0:
        print("Año " +str(year) +" comun")
    else:
        print("Año " +str(year) +" bisiesto")
else:
    print("Año " + str(year) +" No esta dentro del período del calendario Gregoriano")
