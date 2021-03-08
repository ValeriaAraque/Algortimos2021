#Devuelva el cuadrado de cada elemento de la lista
listaNumeros = [1,2,3,4,5]
cuadrado = lambda numero = 0 : numero **2
listaCuadrados = list(map(cuadrado,listaNumeros))
print (listaCuadrados)

#Divida a todos los elementos de la lista por el mayor numero de la lista
listaNumeros = [1,2,3,4,5]
division = lambda numero = 0 : numero/max(listaNumeros)
listaDivision = list(map(division,listaNumeros))
print (listaDivision)

#Le reste un numero n a la lista
listaNumeros = [1,2,3,4,5]
restante = 1
resta = lambda numero = 0 : numero - restante
listaResta = list(map(resta,listaNumeros))
print (listaResta)

#Le sume un numero n a la lista
listaNumeros = [1,2,3,4,5]
suma = lambda numero= 0 : numero +1
listaSuma = list(map(suma,listaNumeros))
print (listaSuma)

#Todos los elementos multiplicados por 5
listaNumeros = [1,2,3,4,5]
multiplicacion = lambda numero = 0 : numero *5
listaMultiplicacion = list(map(multiplicacion,listaNumeros))
print (listaMultiplicacion)