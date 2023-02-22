import sys

n=int(sys.argv[1])

suma=0

if n <= 0:
	print("Error")
	exit()
else:
	for i in range(1, n+1):
		p=i**2
		suma=suma+p
	print(suma)