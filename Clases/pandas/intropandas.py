import pandas as pd
listaVariada = ['a',1,2,4.6]
print (listaVariada)
seriesPandas = pd.Series ([1,2,5])
print (seriesPandas)
seriesPandas = pd.Series ([1,2,'a'])
print (seriesPandas)
dicGanancias = {}
dicGanancias ['Enero'] = 4300
dicGanancias ['Febrero'] = 4545
dicGanancias ['Marzo'] = 2324
dicGanancias ['Abril'] = 1244
seriesGananciaPorMes = pd.Series ([4300,4545,2324,1244])
print (seriesGananciaPorMes)
seriesGananciaPorMesDic = pd.Series (dicGanancias)
print ('Enero',seriesGananciaPorMesDic ['Enero'])
print (seriesGananciaPorMesDic ['Enero': 'Marzo'])
print (seriesGananciaPorMesDic ['Febrero': 'Marzo'])

nombres = [['Juan','Karla'], ['Arturo', 'Laura']]
dataFrameNombres = pd.DataFrame(nombres)
print (dataFrameNombres)

matrizEstudiantesDic = {
                        'Grupo1' :['Karla', 'Mario', 'Laura'],
                        'Grupo2' :['Santi', 'Arturo', 'Vale'],
                        'Grupo3' :['Juan', 'Melany', 'Laura'],
                        'Grupo4' :['Mafer', 'Esteban','Daniel'],
}
dataFrameNombresDic = pd.DataFrame(matrizEstudiantesDic)
print (dataFrameNombres)
print ("#"*60)
print (dataFrameNombresDic ['Grupo2'])
print ("#"*60)
print (dataFrameNombresDic ['Grupo1'])
print ("#"*60)
print (dataFrameNombresDic)
print (dataFrameNombresDic.iloc[1:2])
print (dataFrameNombresDic.iloc[1:])

dicVentasPorMes = {
    'Marzo (millones de pesos)'  :[1234,4235,2356],
    'Abril (millones de pesos)' :[1234,423342,223356],
    'Mayo  (millones de pesos)' :[4123,4537,6577]
}
dataFrameVentas = pd.DataFrame (dicVentasPorMes, index = ['Tomates','Papa','Yuca'])
print (dataFrameVentas)
print (dataFrameVentas.iloc [2])
#Serie con ganancias durane un año
#Inventar ejercicio papas, yucas y tomates para todo el año