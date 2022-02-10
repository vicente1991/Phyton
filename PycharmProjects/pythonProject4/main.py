asignaturas = ["Lengua", "EF", "Tutoria", "Conocimiento del Medio","Matemáticas" ]
print(asignaturas)

asignaturas = ["Lengua", "EF", "Tutoria", "Conocimiento del Medio", "Matemáticas"]
for subject in asignaturas:
    print("Yo estudio " + subject)

asignaturas = ["Lengua", "EF", "Tutoria", "Conocimiento del Medio", "Matemáticas"]
notas = []
for asig in asignaturas:
    calificacion = input("¿Qué nota sacaste en " + asig + "?")
    notas.append(calificacion)
for i in range(len(asignaturas)):
    print("En " + asignaturas[i] + " has sacado " + notas[i])

loteria = []
for i in range(6):
    loteria.append(int(input("Introduce un número ganador: ")))
loteria.sort()
print("Los números ganadores son " + str(loteria))

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(1, 11):
    print(num[-i], end=", ")