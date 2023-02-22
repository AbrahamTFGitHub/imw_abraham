import sys

money = int(sys.argv[1])

r = money//50

if r > 0:
    print("Cantidad de billetes de 50€ = " +str(r))
    
r1= money%50
    
e = r1//20

if e > 0:
    print("Cantidad de billetes de 20€ = " +str(e))
    
r2= money%20
    
f = r2//10

if f > 0:
    print("Cantidad de billetes de 10€ = " +str(f))
    
r3= money%10
    
g = r3//5

if g > 0:
    print("Cantidad de billetes de 5€ = " +str(g))

r4= money%5

k = r4//2

if k > 0:
    print("Cantidad de monedas de 2€ = " +str(k))
    
r5= money%2

j = r5//1

if j > 0:
    print("Cantidad de monedas de 1€ = " +str(j))
