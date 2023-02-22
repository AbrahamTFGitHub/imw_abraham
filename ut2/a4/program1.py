import sys

dni=int(sys.argv[1])
palabra='TRWAGMYFPDXBNJZSQVHLCKE'
letra= dni%23

print ("El DNI completo es: "f'{dni}{palabra[letra]}')
