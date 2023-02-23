import sys
from math import sqrt

r = float(input("Radio de entrada = "))

print ("1. Calcular diámetro de la circunferencia") 
print ("2, Calcular perímetro de la circunferencia")
print ("3. Calcular área del circulo")
print ("4. Salir")

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
    print ("Escribe un número del 1 al 4")
 
print ("Finalizado")
