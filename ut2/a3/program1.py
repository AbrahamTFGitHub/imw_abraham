import sys

n=int(sys.argv[1])

if n <= 0:
	print("Error")
	exit()
elif n==1:
	print(n, "Por convenio NO es ni Primo ni Compuesto")
else:
	for i in range(2, n):
		p=n%i
		if p==0:
			print(n, "No es Primo.")
			exit()
	print(n, "Es Primo.")