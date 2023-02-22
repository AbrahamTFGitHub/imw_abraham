import sys
from math import sqrt

a = float (sys.argv[1])

if a in range (0,11):

    if a < 5:
        print ("Suspendido")
    else:
    
        if a in range (5,7):
            print ("Aprobado")
        else:

            if a in range (7,9):
                print ("Notable")
            else:

                if a in range (9,10):
                    print ("Sobresaliente")
                else:

                    if a == 10:
                        print ("Matricula de honor")
                        
else: 
    print ("Introduzca nota entre el 0 y el 10")
