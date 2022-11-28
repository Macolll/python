def ingresar():
    
    nombre=input("ingresa tus nombres: ")
    apellidos=input("ingresa tus apellidos: ")
    edad=input("ingresa tu edad: ")
    return f"\ntus datos son:\nnombres: {nombre}\napellidos: {apellidos}\nedad: {edad} "

print(ingresar())