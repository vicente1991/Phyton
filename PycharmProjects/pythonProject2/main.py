edad = int(input("¿Cuál es tu edad? "))
if edad < 18:
    print ("Eres menor de edad.")
else:
    print("Eres mayor de edad.")

contraseña = "contraseña"
password = input("Introduce la contraseña: ")
if contraseña == password.lower():
    print("La contaseña coincide")
else:
    print("La contraseña no coincide")


dividendo = float(input("Introduce el dividendo: "))
divisor = float(input("Introduce el divisior: "))
if divisor == 0:
    print("No se puede dividir por 0.")
else:
    print(dividendo/divisor)


num = int(input("Introduce un número entero: "))
if num % 2 == 0:
    print("El número " + str(num) + " es par")
else:
    print("El número " + str(num) + " es impar")

edad = int(input("¿Cuál es tu edad? "))
ing = float(input("¿Cuales son tus ingresos mensuales?"))
if edad <= 16 or ing < 1000:
    print("No tienes que cotizar")
else:
    print("Tienes que cotizar")