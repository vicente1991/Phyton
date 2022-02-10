palabra = input("Introduce una palabra: ")
for i in range(10):
    print(palabra)



edad = int(input("¿Cuántos años tienes? "))
for i in range(edad):
    print("Tu cumples " + str(i+1) + " años")



num = int(input("Introduce un número entero: "))
for i in range(1, num+1, 2):
    print(i, end=", ")



n = int(input("Introduce un número entero: "))
for i in range(n, -1, -1):
    print(i, end=", ")


cant = float(input("¿Cantidad a invertir? "))
interes = float(input("¿Interés porcentual anual? "))
años = int(input("¿Años?"))
for i in range(años):
    cant *= 1 + interes / 100
    print("Capital tras " + str(i+1) + " años: " + str(round(cant, 2)))