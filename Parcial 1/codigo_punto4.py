
def contarPalabrasV1(parrafo):
    dictPalabrasOcurrencias = {}
    listaPalabras = parrafo.split()
    for palabra in listaPalabras:
        dictPalabrasOcurrencias[palabra] = listaPalabras.count(palabra)
    return dictPalabrasOcurrencias

def contarPalabrasV2(parrafo):
    dictPalabrasOcurrencias = {}
    listaPalabras = parrafo.split()
    for palabra in listaPalabras:
        dictPalabrasOcurrencias[palabra] = 0
        for i in range (len(listaPalabras)):
            if palabra == listaPalabras[i]:
                dictPalabrasOcurrencias[palabra] += 1
        return dictPalabrasOcurrencias

import time

#Inicio Contar palabras 1
inicio = time.time()
#Instrucciones 
contarPalabrasV1('La justicia sobre la fuerza es la impotencia, la fuerza sin justicia es tiranía. Vale más saber alguna cosa de todo que saberlo todo de una sola cosa. Dos excesos: excluir la razón, no admitir más que la razón. Nuestra naturaleza está en movimiento. El reposo absoluto es la muerte. El hombre tiene ilusiones como el pájaro alas. Eso es lo que lo sostiene. El hombre está dispuesto siempre a negar todo aquello que no comprende. Aquel que duda y no investiga, se torna no sólo infeliz, sino también injusto. A fuerza de hablar de amor, uno llega a enamorarse. ¿De qué le sirve al hombre ganar el mundo si pierde su alma')
#Delta
deltaV1 = time.time () - inicio

#Inicio Contar palabras 2
inicio = time.time()
#Instrucciones
contarPalabrasV2 ('La justicia sobre la fuerza es la impotencia, la fuerza sin justicia es tiranía. Vale más saber alguna cosa de todo que saberlo todo de una sola cosa. Dos excesos: excluir la razón, no admitir más que la razón. Nuestra naturaleza está en movimiento. El reposo absoluto es la muerte. El hombre tiene ilusiones como el pájaro alas. Eso es lo que lo sostiene. El hombre está dispuesto siempre a negar todo aquello que no comprende. Aquel que duda y no investiga, se torna no sólo infeliz, sino también injusto. A fuerza de hablar de amor, uno llega a enamorarse. ¿De qué le sirve al hombre ganar el mundo si pierde su alma')
#Delta
deltaV2 = time.time() - inicio

print (deltaV2)
print (deltaV1)
print (deltaV1 == deltaV2)
print (deltaV1 > deltaV2)
print (deltaV2 > deltaV1)

#Justificacion: Debido a lo que vimos en clase considero que la segunda funcion se demoraria mas ya que tiene un for mas que la primera por lo que se tendria que hacer un proceso adicional