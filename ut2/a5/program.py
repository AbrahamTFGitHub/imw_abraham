import sys


def num_vowels(text):
    v = 0
    for c in text:
        if c in "aeiouAEIOU":
            v = v + 1
    return v

def num_whitespaces(text):
    c = 0
    for i in text: 
        if i == " ": 
            c += 1 
    return c 

def num_digits(text):
    v = 0
    for c in text:
        if c in "0123456789":
            v = v + 1
    return v

def num_words(text):
    num_words = 0
    i=len(text.split())
    num_words = i
    return num_words
            
def reverse(text):
    p = ''.join(reversed(text))
    return p


def length(text):
    x=len(text)
    return x


def halfs(text):
    s1 = text[:len(text)//2]
    s2 = text[len(text)//2:]
    return (s1,s2)


def upper_vowels(text):
    f = ""
    for char in text:
        if char in ('a', 'e', 'i', 'o', 'u'):
            char = char.upper()
            f += char
        else: 
            f += char
    return f


def sorted_by_words(text):
    g = sorted(text.split())
    return g


def length_of_words(text):
    y = [len(text) for text in text.split()]
    return y


if __name__ == '__main__':
    text = sys.argv[1]
    print('Número de vocales:', num_vowels(text))
    print('Número de espacios:', num_whitespaces(text))
    print('Número de dígitos:', num_digits(text))
    print('Número de palabras:' , num_words(text))
    print('El texto al revés:', reverse(text))
    print('Longitud de texto:', length(text))
    print('Texto por la mitad:', halfs(text))
    print('Texto con las vocales en mayusculas:', upper_vowels(text))
    print('Palabras ordenadas alfabéticamente:', sorted_by_words(text))
    print('Longitud de las palabras:', length_of_words(text))