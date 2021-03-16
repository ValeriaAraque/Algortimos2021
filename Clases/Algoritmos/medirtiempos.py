import time
tiempoInicial = time.time()
print ('Hola a todos')
time.sleep (2)
tiempoFinal = time.time()
delta = tiempoFinal - tiempoInicial
print (delta)

#Inicio conteo
tiempoInicial = time.time ()
#Instrucciones
print ('hola a todos')
x = int(input('Ingrese un numero: '))
for i in range (x):
    for j in range (x):
        print (i)
#Cierre de conteo
tiempoFinal = time.time ()
delta = tiempoFinal - tiempoInicial
print (delta)