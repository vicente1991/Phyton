import math
math.sqrt(9)

class Punto:

    def __init__(self, X, Y):
        if X is None & Y is None:
            return 0
        else:
            self.X = X
            self.Y = Y

    def __str__(self):
        return f"Punto: {self.X} {self.Y}"

    def cuadrante(self):
        if self.X==0 & self.Y!=0:
            return print("El punto esta sobre el eje Y")
        if self.X !=0 & self.Y ==0:
            return print("El punto esta sobre el eje X")
        if self.X==0 & self.Y==0:
            return ("El punto esta sobre el origen")
        else:
            if self.X >0 & self.Y >0:
                return ("El punto esta en el cuadrante arriba derecha")
            if self.X >0 & self.Y <0:
                return ("El punto esta en el cuadrante abajo derecha")
            if self.X < 0 & self.Y <0:
                return ("El punto esta en el cuadrante abajo izquierda")
            if self.X < 0 & self.Y < 0:
                return ("El punto esta en el cuadrante arriba izquierda")


    def vector(self,punto2):
        coordenada1= punto2.X-self.X
        coordenada2= punto2.Y-self.Y

        return print("("*coordenada1+","*coordenada2+")")



class Rectangulo:

    inicial=Punto()
    final=Punto()

    def __init__(self,inicial,final):
        if inicial is None & final is None:
            return 0
        else:
            self.inicial=inicial
            self.final=final
    
    def base(self):
        base=self.inicial
        return base
    def altura(self):
        final= self.final
        return final
    def area(self):
        area=self.inicial*self.final
        return area

r1=Rectangulo(4,2)
base= r1.inicial
altura= r1.final
area=r1.area()
print("Su base es:", base)
print("Su altura es:", altura)
print("El area es:",area)
