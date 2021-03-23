import time
import ordenamiento_burbuja as ob
import random as r
import ordenamiento_insercion as oi 

lista = []
for i in range (1200):
    lista.append (r.randint(1,10000))
listaCopia = lista.copy ()
listaCopia2 = lista.copy ()

#Inicio Burbuja
inicio = time.time()
#Instrucciones 
ob.ordenamientoBurbuja (lista)
#Delta
deltaOb = time.time () - inicio

#Inicio Sort
inicio = time.time()
#Instrucciones
listaCopia.sort ()
#Delta
deltaSort = time.time() - inicio

#Inicio Insercion
inicio = time.time()
#Instrucciones
oi.ordenamientoInsercion (lista)
#Delta
deltaOi = time.time () - inicio

print (deltaSort)
print (deltaOb)
print (deltaOi)
print (deltaSort >= deltaOb)
print (deltaSort >= deltaOb)