#Dada una lista de numeros enteros devuelva otra con los numeros divisibles entre 7
listaNumeros1 = [1,2,7,5,14,11,21]
divisiblesSiete = lambda numero = 0 : numero %7 == 0
listaDivSiete = list(filter(divisiblesSiete,listaNumeros1))
print (listaDivSiete)

#Dada una lista de nombres de estudiantes devuelva una con los nombres de un largo menor a 5
listaNombres = ['Valeria','Mario','Laura','Melany','Santiago', 'Ana']
largoNombres = lambda nombres : len (nombres) < 5 
listaLargoNom = list(filter(largoNombres,listaNombres))
print (listaLargoNom)

#Dada una lista de numeros devuelva los pares
listaNumeros = [1,2,7,5,14,11,21,8]
pares = lambda numero : numero %2 == 0
listaPares = list(filter(pares,listaNumeros))
print (listaPares)

#Dada una lista de numeros devuelva los impares
listaNumeros = [1,2,7,5,14,11,21,8]
impares = lambda numero : numero % 2 != 0
listaImpares = list(filter(impares,listaNumeros))
print (listaImpares)

#Dada una lista de nombres devuelva unicamente aquellos que inician con la letra E
listaNombres2 = ['Laura','Daniela','Juan Jose','Elena','Daniel']
nombresE = lambda nombre : nombre [0] == 'E'
listaNombresE = list(filter(nombresE,listaNombres2))
print (listaNombresE)

#Dada una lista de edades solo devuelva los maypres de edad
listaEdades = [12,5,16,34,23,45,67,20]
mayoresEdad = lambda edad : edad >= 18
listaMayoresEdad = list(filter(mayoresEdad,listaEdades))
print (listaMayoresEdad)

#Dada una lista frases devuelvan unicamente aquellas frases que no tengan la palabra odian
listaFrases = ["Amo los animales","Ella no odia nada", "Mi perro odia los truenos"]
odiar = lambda elemento : 'odia' not in elemento
listaFrasesFilter = list(filter(odiar,listaFrases))
print (listaFrasesFilter)