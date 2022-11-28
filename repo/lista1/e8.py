contraseña="llu"
ingresa=input("ingresa tu contraseña")
if(ingresa.isupper()):
    nuevo=ingresa.lower()
    if(nuevo==contraseña):
        print("correcto si coincide ")
    else:
        print("no coincide")