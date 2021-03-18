import time
import ordenamiento_burbuja as ob
import random as r 

lista = []
for i in range (12000):
    lista.append (r.randint(1,10000))
listaCopia = lista.copy ()

#Inicio
inicio = time.time()
#Instrucciones 
ob.ordenamientoBurbuja (lista)
#Delta
deltaOb = time.time () - inicio

#Inicio
inicio = time.time()
#Instrucciones
listaCopia.sort ()
#Delta
deltaSort = time.time() - inicio

print (deltaSort >= deltaOb)