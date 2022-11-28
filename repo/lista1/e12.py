import re
patron = ('[aeiouAEIOU]')

ip = re.compile(patron)
letra=input("ingresa una letra")
if(len(letra)>1):
    print("no se puede procesar el dato")
else:
    if ip.search(letra):
        print("es una vocal")
    else:
        print("no es una vocal")
