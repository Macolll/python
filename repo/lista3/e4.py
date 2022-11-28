import os
def f():
    #1nombre de sistema operativo
    print("\nel nombre del sistema operarivo es: ",os.name)
    #2 ruta actual
    ruta=os.getcwd()
    print("\nla ruta actual es: ",ruta,"\n")

    #3 concatenar de manera inteligente y posteriormente leer archivos
    file_path = os.path.join(ruta,'repo','lista3','ar.txt')
    print("se imprimira el contenido del archivo ar.txt\n")
    with open(file_path,mode='r') as f:
        data = f.readlines()#lee todas las lineas del archi
    
        print(data)
    
    #archivo se cierra de forma automatica
