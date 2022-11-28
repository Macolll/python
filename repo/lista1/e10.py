base=10
mora=int(input("ingresa mora en dias"))
if(mora==1):
    deuda=base+(base*5)/100
elif mora >1 and mora<=30:
    deuda=base+(base*8)/100
else:
    deuda=base+(base*10)/100