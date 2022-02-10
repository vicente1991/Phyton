cadena=input('Dame una cadena de caracteres:')
caracter=input('Dame un caracter:')
while len(caracter)!=1:
    caracter=input('Dame solo un caracter:')
print('En la cadena',cadena,'aparecen ',cadena.count(caracter),'veces el caracter', caracter)