#1
import pandas as pd
dicPacientesTratados = {}
dicPacientesTratados ['Enero'] = 32121
dicPacientesTratados ['Febrero'] = 14564
dicPacientesTratados ['Marzo'] = 65465
dicPacientesTratados ['Abril'] = 85202
dicPacientesTratados ['Mayo'] = 93213
dicPacientesTratados ['Junio'] = 100231
dicPacientesTratados ['Julio'] = 120213
dicPacientesTratados ['Agosto'] = 65421
dicPacientesTratados ['Septiembre'] = 46546
dicPacientesTratados ['Octubre'] = 46547
dicPacientesTratados ['Noviembre'] = 84651
dicPacientesTratados ['Diciembre'] = 140521
seriePacientesTratados = pd.Series (dicPacientesTratados)
print (seriePacientesTratados)

#2 Ganancias cuatrimestre
dicGananciasCuatrimestre = {}
dicGananciasCuatrimestre ['1er Cuatrimestre'] = (seriePacientesTratados ['Enero': 'Abril'])
dicGananciasCuatrimestre ['2ndo Cuatrimestre'] = (seriePacientesTratados ['Mayo': 'Agosto'])
dicGananciasCuatrimestre ['3er Cuatrimestre'] = (seriePacientesTratados ['Septiembre': 'Diciembre'])
seriesGananciasCuatrimestre = pd.Series (dicGananciasCuatrimestre)
print (seriesGananciasCuatrimestre)

#3 Promedio pacientes por mes
from functools import reduce
listaPacientes = [32121,14564,65465,85202,93213,100231,120213,65421,46546,46547,84651,140521]
sumador = lambda acumulado =0 , elemento = 0: acumulado + elemento
promedio = reduce (sumador,listaPacientes)/len (listaPacientes)
print (promedio)

#4
dicEnfermedades = {
    'Enfermedad General' : [32121,14564,65465,85202,93213,100231],
    'COVID-19' : [0,0,223,3453,4543,43643],
    'Traumatismos' : [6545,43243,67657,435435,345345,43543],
    'Cancer' : [6542,4334,4323,34545,5454,7675]
}
dataFrameEnfermedades = pd.DataFrame (dicEnfermedades, index = ['Enero','Febrero','Marzo','Abril','Mayo','Junio'])
print (dataFrameEnfermedades)

#5 Promedio covid abril,mayo,junio
listaCOVID = [3453,4543,43643]
sumador = lambda acumulado =0 , elemento = 0: acumulado + elemento
promedioCOVID = reduce (sumador,listaCOVID)/len (listaCOVID)
print (promedioCOVID)

#6
print ('Primer trimestre traumatismos')
print (dataFrameEnfermedades [['Traumatismos']]['Enero':'Marzo'])

#7
listaPacientesEnGeneral = [32121,14564,65465,85202,93213,100231]
pacientes = lambda pacientes : pacientes > 40000
pacientesEnGeneral = list(filter(pacientes,listaPacientesEnGeneral))
print (pacientesEnGeneral)

#8
listaPacientesCancer = [6541,4334,4323,34545,5454,7675]
porcentaje = lambda pacientes = 0 : pacientes * 0.1
listaPacientes = list (map(porcentaje, listaPacientesCancer))
print (listaPacientes)

#9
listaPacientesTraumatismos = [6545,43243,67657,435435,345345,43543]
sumatoria = lambda acumulado =0 , elemento = 0: acumulado + elemento
sumatoriaTraumatismos = reduce (sumatoria,listaPacientesTraumatismos)
print (sumatoriaTraumatismos)