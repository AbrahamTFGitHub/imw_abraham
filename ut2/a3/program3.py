import sys

a=int(sys.argv[1])

b=int(sys.argv[2])

if a <= 0 or b <= 0:
	print("Error")
	exit()
	
if a<b:
    n=a
else:
    n=b
for n in range(n, 0, -1):
    div_a=a%n
    div_b=b%n
    if div_a==div_b and n>1 and div_a==0 and div_b==0:
        print("El mcd es: "+str(n))
        print("Saliendo...")
        break
    elif n==1:
        print("Los números no tienen el mcd")
        print("Saliendo...")
        break  
