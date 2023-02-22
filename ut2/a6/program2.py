import sys

def m():
    phone_book = {}
    while True:

        print('''
        1. Mostrar lista de contactos.
        2. Añadir contacto: (Nombre y Teléfono).
        3. Borrar contacto: (Nombre).
        4. Salir.
        ''')

        m = input("Elige Opción: ")

        if m == '1':
            show_contacts(phone_book)


        elif m == '2':
            name = input("Nombre del contacto: ")
            if name not in phone_book:
                phone = input("Número de teléfono del contacto: ")
                add_contact(phone_book, name, phone)
            else:
                print("Ha sido añadido. ")


        elif m == '3':
            name = input("Nombre del contacto para borrar: ")
            if name in phone_book:
                remove_contact(phone_book, name)
            else:
                print("El contacto no esta en la lista de contactos. ")

        elif m == '4':
            break

        elif m > '4':
            print("Opción desconocida: ")

def show_contacts(phone_book):
    if phone_book == {}:
        print("La agenda está vacía. Por favor, añade contactos para poder usar el menú.")
    else:
        for name, phone in phone_book.items():
            print(name, ":", phone)

def add_contact(phone_book, name, phone):
    phone_book[name] = phone

def remove_contact(phone_book, name):
    del(phone_book[name])

if __name__ == '__main__':
    m()