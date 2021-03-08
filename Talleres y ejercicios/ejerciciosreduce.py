from functools import reduce
#Obtenga la resta de todos los elementos de una lista
lista1 = [1,2,3,4,5,6]
restarElementos = lambda acumulado = 0, elemento = 0: acumulado - elemento
restar = reduce (restarElementos, lista1)
print (restar)

#Dada una lista de palabras devolver una frase
listaPalabras = ['Hola','me','llamo','Valeria']
unirFrase = lambda frase, palabra : frase + ' ' + palabra
frase = reduce (unirFrase,listaPalabras)
print (frase)

#Dada una lista de numeros enteros entregue la sumatoria de todos elementos tras haber sido divididos por dos
listaEnteros = [1,2,3,4,5,6,7]
suma = lambda acumulado = 0, enteros = 0: round(acumulado + enteros/2,2)
sumatoria = reduce (suma,listaEnteros)
print (sumatoria)

#Devuelva el promedio de una lista de numeros 
listaEnteros = [1,2,3,4,5,6,7]
promedio = lambda acumulado = 0, enteros = 0: round(acumulado + enteros/ len(listaEnteros),2)
promedioEnteros = reduce (promedio,listaEnteros)
print (promedioEnteros)

#Que multiplique todos los elementos de la lista entre si
listaEnteros = [1,2,3,4,5,6,7]
multiplicacion = lambda acumulado = 0, numero = 1: acumulado * numero
multiplicacionEnteros = reduce (multiplicacion,listaEnteros)
print (multiplicacionEnteros)