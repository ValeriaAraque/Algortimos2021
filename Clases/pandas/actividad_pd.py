import pandas as pd
dicGanancias = {}
dicGanancias ['Enero'] = 650000
dicGanancias ['Febrero'] = 650000
dicGanancias ['Marzo'] = 700000
dicGanancias ['Abril'] = 750000
dicGanancias ['Mayo'] = 780000
dicGanancias ['Junio'] = 800000
dicGanancias ['Julio'] = 830000
dicGanancias ['Agosto'] = 850000
dicGanancias ['Septiembre'] = 85000
dicGanancias ['Octubre'] = 900000
dicGanancias ['Noviembre'] = 950000
dicGanancias ['Diciembre'] = 1000000
seriesGananciaPorMes = pd.Series ([650000,650000,700000,750000,780000,800000,830000,850000,850000,900000,950000,1000000])
print (seriesGananciaPorMes)
seriesGananciaPorMesDic = pd.Series (dicGanancias)

dicVentasPorMes = {
    'Enero (miles de pesos)'  :[123400,423500,235600],
    'Febrero (miles de pesos)'  :[223400,400500,205600],
    'Marzo (miles de pesos)'  :[223000,421000,255000],
    'Abril (miles de pesos)' :[223000,523300,223350],
    'Mayo  (miles de pesos)' :[412003,500537,680077]
    'Junio  (miles de pesos)' :[412300,450307,605707]
    'Julio  (miles de pesos)' :[412000,450000,650000]
    'Agosto  (miles de pesos)' :[112000,457000,670000]
    'Septiembre  (miles de pesos)' :[450000,550000,690000]
    'Octubre  (miles de pesos)' :[470000,760000,650000]
    'Noviembre  (miles de pesos)' :[789000,567000,900000]
    'Diciembre  (miles de pesos)' :[776000,345000,679000]
}
dataFrameVentas = pd.DataFrame (dicVentasPorMes, index = ['Tomates','Papa','Yuca'])
print (dataFrameVentas)