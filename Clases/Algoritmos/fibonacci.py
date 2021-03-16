#Fibonacci: 0,1,1,2,3,5,8,13,21

#Preguntas
preguntaNumero = 'Ingrese un numero entero: '
#Mensajes error
errorEntrada = 'Entrada no valida'
#Entradas
numero = None
while (numero == None):
    try:
        numero = int (input(preguntaNumero))
    except ValueError:
        print (errorEntrada)
print (numero)

numeroAnterior = 0
numeroActual = 1
if (numero == 1):
    print (numeroAnterior)
elif (numero == 2):
    print (numeroActual)
else:
    for i in range (2, numero + 1):
        aux = numeroActual
        numeroActual = numeroAnterior + numeroActual
        numeroAnterior = aux
        print (numeroActual)
    print ('Salida', numeroActual)

#Repetir ejercicio
