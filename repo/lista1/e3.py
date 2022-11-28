def ingresar():
    
    n1=float(input("ingresa un primer  valor numerico: "))
    n2=float(input("ingresa un segundo valor numerico: "))
    n3=float(input("ingresa un tercer valor numerico: "))
    suma=n1+n2+n3
    resta=n1-n2-n3
    multi=n1*n2*n3
    return f"\nlos resultados  son:\nsuma: {suma}\nresta: {resta}\nmulti: {multi} "

print(ingresar())