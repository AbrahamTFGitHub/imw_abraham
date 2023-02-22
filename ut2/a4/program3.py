import sys

k = int(sys.argv[1])
j = sys.argv[2]
x, c = 0, 0
chain = j + ' '

if k <= 0:
    print('Solo se aceptan números positivos.')
else:
    for i in j:
        if i != ' ':
            c += 1
        else:
            if c == k:
                x += 1
                c = 0
            else:
                c = 0

print(f'Hay {x} palabras de tamaño {k}')