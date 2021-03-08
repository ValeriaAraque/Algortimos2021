#lambda entradas :accion 
#Funcion que devuelve exponente de un numero dado
exponente = lambda base,exponente : print (base ** exponente)
exponente (5,2)

#Muestre en pantalla n veces un string ingresado
string = lambda frase,cantidad : print( frase *cantidad)
string ("Hola me gusta programar, ",5)

#Muestre en pantalla el maximo numero de dos listas ingresadas
lista1 = [2,34,5,67,17]
lista2 = [10,5,24,81]
maximo = lambda x = [], y = [] : print (max(x),max(y))
maximo (lista1,lista2)

#Devuelva verdadero o falso dependiendo si un numero es par o no
par = lambda numero : numero%2 == 0 
print (par (11))
print (par (10))

#Devuelva verdadero o falso dependiendo si un numero es impar o no
impar = lambda numero : numero%2 != 0 
print (impar(2))
print (impar (5))

#Que devuelva la union de dos palabras
union = lambda palabra1 ,palabra2 : palabra1 + ' ' + palabra2 
print (union ("Papas", "Fritas"))

#Que dado un nombre salude a la persona ingresada
nombre = input("Ingrese su nombre: ")
saludar = lambda nombre : print(f'Hola {nombre}, bienvenida')
saludar(nombre)

#Que dada una palabra devuelva el largo de la misma
palabra = 'Perrito'
largoPalabra = lambda palabra: len(palabra)
print (largoPalabra (palabra))

#Que utilizando la anterior muestre en pantalla el resultado
mostrarLargoPalabra = lambda funcion, palabra : print (funcion(palabra))
mostrarLargoPalabra(largoPalabra,palabra)

#Devuelva el area de un triangulo dada su base y su altura
areaTriangulo = lambda base,altura : base*altura/2
print (areaTriangulo(3,5))

#Calcule el imc sabiendo la altura y el peso imc = peso/altura^2
calcularIMC = lambda peso,altura : round(peso/altura**2,2)
print (calcularIMC(50,1.63))
