class Producto:
    # Constructor de clase
    def __init__(self, nombre,marca, precio):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
      
    def __str__(self):
        return f"nombre: {self.nombre} ,marca: {self.marca}, precio: s/.{self.precio}.00" 

class Catalogo:

    listaProductos = []  

    def __init__(self, pro):
        self.listaProductos.append(pro)

    def agregar(self, p):  
        self.listaProductos.append(p)

    def mostrar(self):
        for ob in self.listaProductos:
            print(ob)  #str

