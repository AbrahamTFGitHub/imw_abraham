import sys
from math import sqrt

a = float (sys.argv[1])
b = float (sys.argv[2])
c = float (sys.argv[3])

x = -c/b

if a==0:
    print("Como A es 0, X es igual a:" +str(x))
else:

    if ((b**2)-4*a*c) < 0:
      print("La solución de la ecuación es con numeros complejos")

    else:
      x1 = (-b+sqrt(b**2-(4*a*c)))/(2*a)
      x2 = (-b-sqrt(b**2-(4*a*c)))/(2*a)
      print("X1 es igual a:"+str(x1))
      print("X2 es igual a:"+str(x2))
