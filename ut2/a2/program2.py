import sys
from math import sqrt

x1 = float (sys.argv[1])
y1 = float (sys.argv[2])
x2 = float (sys.argv[3])
y2 = float (sys.argv[4])
x3 = float (sys.argv[5])
y3 = float (sys.argv[6])
d = sqrt((x1-x2)**2+(y1-y2)**2)
d2 = sqrt((x1-x3)**2+(y1-y3)**2)

if d < d2:
    print ("Lo más cercano a ("+str(x1)+","+str(y1)+ ")es ("+str(x2)+","+str(y2)+ ")y esta a una distancia de " +str(d))
else:
    print ("Lo más cercano a ("+str(x1)+","+str(y1)+ ")es ("+str(x3)+","+str(y3)+ ")y esta a una distancia de " +str(d2))


