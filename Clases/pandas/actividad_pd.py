import pandas as pd
dicGanancias={}
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