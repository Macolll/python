#pir2
import math
def ingresar():
    
    r=float(input("ingresa el radio de circulo: "))
    area=r*r*math.pi
    return f"\nel area es: {area} "

print(ingresar())
