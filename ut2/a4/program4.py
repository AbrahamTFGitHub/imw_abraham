import sys

p = sys.argv[1:]
v = len(p)
r = 0

for i in p:
    i = float(i)
    r += i
result = r / v
print(f"La media de los valores es: {result}")