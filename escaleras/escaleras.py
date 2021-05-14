'''
    No estaba seguro de si solo mostrar la cantidad de casos posibles o también como
    seria caso por caso como me mostraron en el ejemplo.

    Asi que diseñe un algoritmo que a pesar de ser mas extenso hace los 2
'''

from itertools import permutations

numEscalones = int(input("ingresa la cantidad de escalones: "))
class Escalera:
    def __init__(self, escalones):
        self.escalones = escalones
    
    def formaMasRapidaDeSubir(self):
        """
            Busca la forma mas rapida de subir la escalera
        """
        formaDeSubir= []
        numEscalones = self.escalones
        while numEscalones > 0:
            if numEscalones >= 2:
                formaDeSubir.append("Subir 2 escalon")
                numEscalones -= 2
            else:
                if numEscalones == 1:
                    formaDeSubir.append("Subir 1 escalon")
                    numEscalones -= 1
        return formaDeSubir

    def pasarMinimoEscalon(self):
        """
            Recibe la forma mas rápida y retorna un array multidimensional
            con la forma mas rápida hasta la mas lenta de subir la escalera
        """
        formaDeSubir = self.formaMasRapidaDeSubir() 
        formaDeSubirCopia = formaDeSubir[:]
        formasAlternas = []
        formasAlternas.append(formaDeSubirCopia[:])
        
        for forma in formaDeSubir:
            if forma == "Subir 2 escalon": 
                formaNueva = formaDeSubirCopia
                formaNueva.pop(0)
                formaNueva.append("Subir 1 escalon")
                formaNueva.append("Subir 1 escalon")
                formasAlternas.append(formaNueva[:])
        return formasAlternas

    def permutarArray(self):
        """
            recibe el array multidimensional de la función anterior y permuta en una lista cada uno
            todas las posibles combinaciones que tenga
        """

        formasAlternas = self.pasarMinimoEscalon()
        todasLasFormas = []  
        for formaAlterna in formasAlternas:
            for formaAlterna in permutations(formaAlterna):
                todasLasFormas+=[formaAlterna[:]]
        return todasLasFormas

    def mostrarTotalCasos(self):
        """
            Recibe la lista permutada y la recorre mostrando todas las formas de subir la escalera que hay
        """

        todasLasFormas = self.permutarArray()
        todasLasFormas = set(todasLasFormas)
        print("la cantidad de formas que hay de subir la escalera son " + str(len(todasLasFormas)) + " y son: \n")
        i = 1
        for formas in todasLasFormas:
            print("opcion " + str(i) + ": ")
            i+=1
            for forma in formas:
                print(forma)
            print(" \n  ")

    def casosTotalesSimple(self):
        """
            genera la cantidad maxima de posiblidades que tiene para subir la escalera
        """

        numEscalones = self.escalones
        if numEscalones < 1:
            return "`El número de escalones debe ser un número positivo"
        a = 0
        b = 1
        index = 1
        while index<=numEscalones+1:
            next = a + b
            a = b
            b = next
            index += 1
        return a

try:
    escalera = Escalera(numEscalones)
    casos = escalera.casosTotalesSimple()
    res = input(f"Las formas total de subir la escalera son: {casos} desea ver las posibles combinaciones? \n 1) Si. \n o cualquier otra tecla para salir. \n ")

    if res == "1":
        escalera.mostrarTotalCasos()
except:
    print("lo siento hay un error en el programa")
    
print("gracias por tu visita")