import csv
import sys

with open('climatologia.csv', newline='', encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile)
    argument = sys.argv[1]
    city = False

    try:
        for column in reader:

            if argument == column['provincia']:
                city = True
                print(column['provincia'], round(float(column['temperatura_maxima'])))

        if city == False:
            raise Exception("No existe ninguna ciudad: " + argument)
    except Exception as cityNotFound:
        print(cityNotFound)