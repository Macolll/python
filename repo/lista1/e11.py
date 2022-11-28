global n1
global n2
n1=(input("ingresa el primer valor numerico: "))

def isfloatn1():
    
    try:
        
        float(n1)
        return True
    except ValueError:
        return False

while(isfloatn1()==False):
    n1=(input("\ningresa correctamente el primer valor numerico: "))
    def isfloatn1():

        try:

            float(n1)
            return True
        except ValueError:
            return False
n1=float(n1)
n2=(input("ingresa el segundo valor numerico: "))
def isfloatn2():
    try:
        float(n2)
        return True
    except ValueError:
        return False

while(isfloatn2()==False):
    n2=(input("\ningresa correctamente el segundo valor numerico: "))
    def isfloatn2():
        try:
            float(n2)
            return True
        except ValueError:
            return False
n2=float(n2)
o=input("""ingresa lo que desea realizar con dichos numeros:
a)Mostrar una suma de los dos números
b)Mostrar una resta de los dos números (el primero menos el segundo)
c)Mostrar una multiplicación de los dos números
""")
if(o=="a"):
    print(n1+n2)
elif o=="b":
    print(n1-n2)
else:
    print(n1*n2)