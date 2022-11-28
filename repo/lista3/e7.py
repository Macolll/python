import requests

def reque():

    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat' #tipo cambio sunat

    # 1. conectarme al sitio
    response = requests.get(url)
    # 2.-parsear a  JSON

    res=response.json()


    # 3. Recupero valor tipo cambio - compra - venta
    dolar_compra = res['compra']
    dolar_venta = res['venta']


    cantidad=float(input("ingrese la cantidad a comprar"))

    print("el valor de cantidad*dolar_compra es: ",cantidad*dolar_compra)
