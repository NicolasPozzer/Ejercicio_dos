class Animal:
    def comer(self):
        print("Comiendo...")

class Mamifero(Animal):
    def amamantar(self):
        print("Amamantando....")

class Ave(Animal):
    def volar(self):
        print("volando....")


class Murcielago(Mamifero, Ave):
    pass

murcielago = Murcielago()
murcielago.comer() #Tambien puede comer aunque sea un metodo de Animal
#                       ya que AVE hereda de Animal.
murcielago.amamantar()
murcielago.volar()