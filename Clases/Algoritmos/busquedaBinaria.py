def busquedaBinaria (lista,encontrar):
    '''Busqueda binaria 
        Se ingresa una lista y un valor a encontrar
        Y entonces se devuelve si lo encontro o no
    '''
    isInList = False
    lista.sort()
    izq = 0
    der = len(lista) -1
    while izq <= der and isInList == False:
        print (lista)
        medio = (izq+der)//2
        print ('Calculo medio', (izq+der)//2)
        print (f'Valor izquierda {izq}, valor medio {medio}, valor derecha {der} ')

        if lista [medio] == encontrar:
            isInList = True
        elif lista [medio] > encontrar:
            der = medio -1
        else:
            izq = medio +1
    return isInList

listaEntrada = [2,12,34,5,11,59,4,3,1]
valorEncontrar = int(input('Ingresar un numero: '))
print(busquedaBinaria (listaEntrada,valorEncontrar))