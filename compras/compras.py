from datetime import datetime
from datetime import timedelta
import json

class Compras:
    def __init__(self, compras):
        self.compras = compras

    def anidarCompras(self):
        """
            Genera los productos y su fecha de compra en un diccionario dentro de un array 
        """

        comprasFiltradas = []
        dicFechas = []
        for compra in self.compras:
            for producto in compra["products"]:
                if producto["name"] in comprasFiltradas:
                    for dicFecha in dicFechas:
                        if dicFecha["producto"]==producto["name"]:
                            dicFecha["fechas"].append(compra["date"])
                else:
                    comprasFiltradas.append(producto["name"])
                    dicFechas.append({"producto":producto["name"], "fechas":[compra["date"]]})
        return dicFechas

    def diferenciaDeDias(self):

        """
            saca la diferencia de días que hay entre las compras de cada producto ejecutando la función
            anterior para recibir el diccionario a comparar.
    	    Saca una media de días entre la diferencia de las compras de cada producto y suma esos días
            a su ultima compra para estimar cuando podrá volver a comprar el cliente 
        """

        dicFechas = self.anidarCompras()
        for dicFecha in dicFechas:
            if len(dicFecha["fechas"]) > 1:
                guardarPrimerFecha = True
                diferenciasDeDias = []


                for fecha in dicFecha["fechas"]: 
                    fecha = datetime.strptime(fecha, '%Y-%m-%d')

                    if guardarPrimerFecha:
                        fechaAComprar = fecha
                        guardarPrimerFecha = False
                    else:
                        diferenciaDeDias = (fecha - fechaAComprar).days
                        fechaAComprar = fecha
                        diferenciasDeDias.append(int(diferenciaDeDias))

                DiasDeDiferencia = sum(diferenciasDeDias)/len(diferenciasDeDias)
                proximaCompra = fecha + timedelta(days=DiasDeDiferencia)

                print("su ultima compra de ", dicFecha["producto"], " fue el ", fecha, "la próxima podría ser ", proximaCompra)

      

with open('purchases.json') as file:
    jsonResponse = json.load(file)
    compras = jsonResponse["customer"]["purchases"]

compras = Compras(compras)
compras.diferenciaDeDias()


  
