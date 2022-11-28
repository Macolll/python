class Gato:
    def __init__(self,edad,nombre):
        self.edad=edad
        self.nombre=nombre
        
    def describe_gato(self):
        print(f"el gato se llama {self.nombre} y tiene {self.edad} años")
       
   
 
g=Gato("2","benito")
g.describe_gato()