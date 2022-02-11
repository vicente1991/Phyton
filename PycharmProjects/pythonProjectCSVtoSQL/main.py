import sqlite3
import csv

contactos = [
    ("Manuel", "Desarrollador Web", "manuel@ejemplo.com"),
    ("Lorena", "Gestora de proyectos", "lorena@ejemplo.com"),
    ("Javier", "Analista de datos", "javier@ejemplo.com"),
    ("Marta", "Experta en Python", "marta@ejemplo.com")
]

with open("contactos.csv", "w", newline="\n") as csvfile:
    campos = ["nombre", "empleo", "email"]
    writer = csv.DictWriter(csvfile, fieldnames=campos)
    writer.writeheader()
    for nombre, empleo, email in contactos:
        writer.writerow({
            "nombre": nombre, "empleo": empleo, "email": email
        })


connection = sqlite3.connect('contactos.sqlite')
cursor = connection.cursor()
cursor.execute('DROP TABLE IF EXISTS contactos')
cursor.execute('''
CREATE TABLE "contactos"(
        "nombre" TEXT,
        "empleo" TEXT,
        "email" TEXT
)''')

with open ('contactos.csv', encoding="utf8") as f:
    reader = csv.reader(f, delimiter =",")
    columns = next(reader)
    query = 'insert into contactos({0}) values ({1})'
    query = query.format(','.join(columns), ','.join('?' * len(columns)))
    cursor = connection.cursor()
    for data in reader:
        cursor.execute(query, data)
    connection.commit()


#Parte2

import csv
import sqlite3


conn = sqlite3.connect('contactos.sqlite')

cursor = conn.cursor()
cursor.execute("select * from contactos;")
with open("contactos2.csv", "w", newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([i[0] for i in cursor.description])
    csv_writer.writerows(cursor)

