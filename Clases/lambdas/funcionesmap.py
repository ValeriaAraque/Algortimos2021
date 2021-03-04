lista = [2,25,34,65,8]
potenciador = lambda valor = 0 : valor **2
print (potenciador(4))
listaCuadrados = list (map(potenciador, lista))
print (listaCuadrados)

def potenciador2 (lista):
    listaCuadrados2 = []
    for elemento in lista:
        valor = elemento**2
        listaCuadrados2.append (valor)
    return listaCuadrados2

lista3 = [2,24,5,45,122,3]
listaCuadrados2 = list(map(potenciador,lista3))
print (listaCuadrados2)

retornarListaCuadrados = lambda listaEntrada = [] : list(map(potenciador, listaEntrada))
lista4 = [2,34,35,35,2,1,4]
listaCuadrados4 = retornarListaCuadrados (lista4)
print (listaCuadrados4)

n = int (input ('Ingrese valor a restar :'))
restarN = lambda valor: valor - n
print (restarN(3))
restarNLista = list (map(restarN,lista4))
print(restarNLista)

#Normalizar
mayor = max (lista4)
dividir = lambda valor = 0 : round(valor/mayor,2)
listaNormalizada = list (map(dividir,lista4))
print (listaNormalizada)

#IMC
pesos = [56,77,85,46,89]
estaturas = [1.66,1.77,1.85,1.46,1.89]

imc = lambda peso = 0, estatura = 1: round(peso/ estatura**2,2)
imcListas = list (map(imc,pesos,estaturas))
print (imcListas)

#Area de un triangulo
bases = [2,34,2,5,345,9]
alturas = [23,345,6,67,23]
divisores = [2,2,2,2,2]
calcularAreaTriangulo = lambda base = 0 , altura = 0, divisores = 1: base*altura/divisores
listaAreasTriangulos = list (map(calcularAreaTriangulo, bases, alturas,divisores))
print (listaAreasTriangulos)

print (sum(bases))

#Funciones reduce
from functools import reduce
sumarElementos = lambda acumulado = 0, elemento = 0: acumulado + elemento
sumar = reduce (sumarElementos, bases)
print (sumar)

multiplicarElementos = lambda acumulado = 0, elemento = 1 : acumulado*elemento
multiplicar = reduce (multiplicarElementos, bases)
print (multiplicar)

print (multiplicar/sumar)