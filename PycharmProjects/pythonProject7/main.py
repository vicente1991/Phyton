class Vehiculo():
    def init(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas


class Coche(Vehiculo):
    def init(self, color, ruedas, velocidad, cilindrada):
        super().init(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada


class Bicicleta(Vehiculo):
    def init(self, color, ruedas, tipo):
        super().init(color, ruedas)
        self.tipo = tipo


class Camioneta(Coche):
    def init(self, color, ruedas, velocidad, cilindrada, carga):
        super().init(color, ruedas, velocidad, cilindrada)
        self.carga = carga


class Motocicleta(Bicicleta):
    def init(self, color, ruedas, tipo, velocidad, cilindrada):
        super().init(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

def catalogar(lista, ruedas=4):

    count = 0
    for vehiculo in lista:

        if ruedas==vehiculo.ruedas:
            count = count + 1

            print(type(vehiculo).name, vehiculo.dict, )
            print("Se encontraron", count, "vehículos con ", ruedas, " ruedas:")


a = Camioneta("Rojo", 8, 120, 400, 500)

b = Coche("Rojo", 4, 120, 800)

c = Bicicleta("Rojo", 2, "Mountain Bike")

d = Coche("Amarillo", 4, 150, 800)

e = Motocicleta("Rojo", 2, "Harley Davison", 150, 200)

lista_vehiculos = [a, b, c, d, e]

catalogar(lista_vehiculos, 4)