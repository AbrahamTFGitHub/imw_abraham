import sys

n=int(sys.argv[1])

mylist=[]

if n < 0:
	print("Error")
	exit()
elif n >= 0 and n <= 1:
	if n==0:
		print("0! = 1")
	else:
		print("1! = 1")
else:
	for i in range(n, 0, -1):
		mylist.append(i)
	p=mylist[0]*mylist[1]
	for o in range(n-2, 0, -1):
		p=p*o
	print(str(n)+"! =",p)