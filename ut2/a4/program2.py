import random

NUCLEOBASES = "TAGC"
DNA_SIZE = 100

a=0
g=0
c=0
t=0
sequence = ''.join([random.choice(NUCLEOBASES) for i in range(DNA_SIZE)])

for n in sequence:
    if n =='A':
        a+=1
    elif n =='G':
        g+=1
    elif n =='C':
        c+=1
    elif n =='T':
        t+=1

print(f'''
Adenine: {a}
Guanine: {g}
Cytosine: {c}
Thymine: {t}
''')
