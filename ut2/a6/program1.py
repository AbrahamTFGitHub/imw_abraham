import sys
sentence = sys.argv[1]

def count_words(sentence):
    summary = {}
    palabras = sentence.split(" ")

    for palabra in palabras:
        if palabra in summary:
            summary[palabra] += 1
        else:
            summary[palabra] = 1
        
    return summary
if __name__ == '__main__':
    r = count_words(sentence)
    for palabra, x in r.items():
        print(f'{palabra}: {x}')

