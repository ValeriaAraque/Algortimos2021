#Crear un elemento donde muestre las ventas mes a mes de una empresa durante un año
import pandas as pd 
dicEarningsPerYear = {}
dicEarningsPerYear ['Enero'] = 123456
dicEarningsPerYear ['Febrero'] = 203456
dicEarningsPerYear ['Marzo'] = 789456
dicEarningsPerYear ['Abril'] = 223456
dicEarningsPerYear ['Mayo'] = 123456
dicEarningsPerYear ['Junio'] = 124056
dicEarningsPerYear ['Julio'] = 123456
dicEarningsPerYear ['Agosto'] = 123456
dicEarningsPerYear ['Septiembre'] = 123556
dicEarningsPerYear ['Octubre'] = 123470
dicEarningsPerYear ['Noviembre'] = 123456
dicEarningsPerYear ['Diciembre'] = 450456
serieEarningsPerYear = pd.Series (dicEarningsPerYear)
print (serieEarningsPerYear)

#Muestren en pantalla las ganancias por trimestre
print ('Primer trimestre')
print (serieEarningsPerYear ['Enero': 'Marzo'])
print ('Segundo semestre')
print (sum(serieEarningsPerYear ['Julio': 'Septiembre']))
dicGananciasTrimestrales = {}
dicGananciasTrimestrales ['1er Trimestre'] = sum (serieEarningsPerYear ['Enero': 'Marzo'])
dicGananciasTrimestrales ['1er Trimestre'] = sum (serieEarningsPerYear ['Abril': 'Junio'])
dicGananciasTrimestrales ['1er Trimestre'] = sum (serieEarningsPerYear ['Julio': 'Septiembre'])
dicGananciasTrimestrales ['1er Trimestre'] = sum (serieEarningsPerYear ['Octubre': 'Diciembre'])
seriesGananciasTrimestrales = pd.Series (dicGananciasTrimestrales)
print (seriesGananciasTrimestrales)
print (sum(serieEarningsPerYear))

#Ganancias por mes por departamento antioquia, amazonas, cundinamarca
dicGananciasPorDepartamento = {
    'Antioquia' : [1234,567,345,674,789,357],
    'Amazonas': [432,678,467,345,876,532],
    'Cundinamarca': [532,378,457,455,876,532]
}
listaMeses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio']
dataFrameGananciasPorDepartamento = pd.DataFrame (dicGananciasPorDepartamento,index=listaMeses)
print (dataFrameGananciasPorDepartamento)

print (dataFrameGananciasPorDepartamento[['Antioquia','Amazonas']]['Febrero':'Abril'])