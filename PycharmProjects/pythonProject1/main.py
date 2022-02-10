nombre = input("¿Cómo te llamas? ")
n = input("Introduce un número: ")
print((nombre + "\n") * int(n))

nombre = input("¿Cómo te llamas? ")
print(nombre.lower())
print(nombre.upper())
print(nombre.title())

nombre = input("¿Cual es tu nombre para saber su numero de letras? ")
print(nombre.upper() + " tiene " + str(len(nombre)) + " letras")

tel = input("Introduce tu numero teléfono con formato +xx-xxxxxxxxx-xx: ")
print('El número de teléfono es ', tel[4:-3])

palabra = input("Introduce una palabra: ")
print(palabra[::-1])