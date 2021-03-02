import numpy as np
lista = [1,2,3,4]
listaC = []
for i in range (200,800,2):
    listaC.append (i)
print (listaC)
listaN = np.arange (200,801,2)
listaNu = np.arange (1,11,1)
print (listaN)
print (listaN [:101])

print (listaNu)
print (listaNu[::2])
listaNu[::2]= 200
print(listaNu)

#Indexacion logica
edades = [14,23,34,56,11,8,23]
edades = np.array (edades)
indEdades = edades > 18
print (edades)
print (indEdades)
totalMayorEdad = np.sum (indEdades)
print (totalMayorEdad)

indEdades2 = edades == 23
indEdades3 = edades == 54
indEdades4 = indEdades2 | indEdades3
print (indEdades2)
print (indEdades3)
print (indEdades4)
print (np.sum (indEdades4))

#Entre 23 y 50
indEdadesIntervalo1 = edades >= 23
indEdadesIntervalo2 = edades <= 50
print ('#'*30)
print (indEdadesIntervalo2)
print (indEdadesIntervalo1)
indEdadesIntervalo = indEdadesIntervalo1 & indEdadesIntervalo2
print (indEdadesIntervalo)
print (np.sum(indEdadesIntervalo))

#Promedio
acum= 0
for elemento in edades :
    acum += elemento

print (acum/len(edades))
print (np.mean(edades))
print ('#'*30)
#---------mama--------#
print ('#'*30)
mamas = [58,54,89,50,91,67,48]
mamas = np.array (mamas)
hijosMayores30 = edades > 30
print (hijosMayores30)
print (mamas [hijosMayores30])
print (mamas)
print (np.mean (mamas[hijosMayores30]))
print ('#'*30)
#Matriz Numpy
edadesHijos = np.array ([14,18,22,24])
edadesMamas = np.array ([45,54,67,74])
childrenMoms = np.array ([edadesHijos,edadesMamas])
print (childrenMoms)
print ('#'*30)
#Transponer Matriz
indKids = childrenMoms[:][0] >= 18
print (childrenMoms.transpose())
print (np.sum(indKids))
print ('#'*30)
print (np.mean(childrenMoms[1][indKids]))
print (indKids)

#Ordenando listas
print ('#'*30)
listaEdades = [12,234,54,6,123,54]
#listaEdades.sort ()
print (listaEdades)
listaEdadesNp = np.array(listaEdades)
listaEdadesNpOrd = np.sort (listaEdadesNp)
print (listaEdadesNpOrd)
print ('El que tiene mas años es ...', max (listaEdades))
print ('El que tiene menos años es ...', min (listaEdades))

#----Mayor y minimo
print ('El que tiene mas años es ...',np.max (listaEdadesNp))
print ('El que tiene menos años es ...',np.min (listaEdadesNp))
#----Mayor a 12
mayoresADoce = listaEdadesNp > 12
print (listaEdadesNp [mayoresADoce])
mayoresAOcho = np.where(listaEdadesNp>8)
print (mayoresADoce)
print (mayoresAOcho)
print (listaEdadesNp[mayoresAOcho[0]])