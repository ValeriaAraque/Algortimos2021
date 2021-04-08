def busquedaBinaria (lista,encontrar):
    '''Busqueda binaria 
        Se ingresa una lista y un valor a encontrar
        Y entonces se devuelve si lo encontro o no
    '''
    lista.sort()
    isInList = False
    izq = 0
    der = len(lista) -1
    while izq <= der and isInList == False:
        medio = (izq+der)//2
        if lista [medio] == encontrar:
            isInList = True
        elif lista [medio] > encontrar:
            der = medio -1
        else:
            izq = medio +1
    return isInList
