class Animal:
    def __init__(self,nombre):
        self.nombre=nombre
    def sonido(self):

        print(f"hola soy: {self.nombre} y nosostros los animales emitimos distintos sonidos")
    def __str__(self):
        return "los animales emiten distintos sonidos"


class Perro(Animal):
    def __init__(self,nombre):
        super().__init__(nombre)
    def sonido(self):
        print(f"hola me llamo: {self.nombre} y hago guau guau")
    def __str__(self):
        return "los perros hacen guau guau"

class Gato(Animal):
    def __init__(self,nombre):
        super().__init__(nombre)
    def sonido(self):
        print(f"hola me llamo: {self.nombre} y hago miau miau")
    def __str__(self):
        return "los gatos hacen miau miau"

