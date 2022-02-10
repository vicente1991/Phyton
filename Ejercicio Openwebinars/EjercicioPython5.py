indicador= False
for var in range(1,6):
    num = int(input("Dime un numero: "))
    if num % 2 == 0:
        indicador= True
if indicador:
    print("Has introducido algun numero par ")
else:
    print("Has introducido ningun numero par")
