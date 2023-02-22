import sys
from math import sqrt

r = float(input("Radio de entrada = "))

print ("1. Calcular el diámetro de la circunferencia") 
print ("2, Calcular el perímetro de la circunferencia")
print ("3. Calcular el área del circulo")
print ("4. para salir")

opcion = input("Eliga una opcion: ")
d = 2*r
p = 2*3.1416*r
a = 3.1416*r**2
  
if opcion == "1":
    print ("El diámetro es = " +str(d))
elif opcion == "2":
    print ("El perímetro es = " +str(p))
elif opcion == "3":
    print("El área es = " +str(a))
elif opcion == "4":
    salir = True
else:
    print ("Introduce un numero entre 1 y el 4")
 
print ("Finalizado")
