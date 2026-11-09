# Importar las librerias
import numpy as np
import pandas as pd
print("Analisis de datos de empleados (Arath Valenzuela NC:0148)")
empleados = {
    "Empleado": ["Elena", "Sergio", "Lucia", "Gonzalo", "Valeria", "Diego"],
    "Departamento": ["Ventas", "IT", "HR", "IT", "Ventas", "Finanzas"],
    "Horas_Capacitacion": [40, 80, 25, 60, 90, 15],
    "Evaluacion_Desempeno": [8.5, 9.2, 7.0, 8.8, 9.6, 6.5]}

df = pd.DataFrame(empleados)
print(df)

print("-----------+ Agrupar por una sola columna (Empleados) +-----------")
agrupado = df.groupby('Departamento')
print(agrupado)

print("-----------+ Por agregación +-----------")
# Horas de capacitacion de cada empleado
print(agrupado['Horas_Capacitacion'].mean())
# Evaluacion del desempeño de cada empleado
print(agrupado['Evaluacion_Desempeno'].max())


print("--Arath---------+ Parte 2 +---------0148--")
print("+--+--+-+ Agregaciones multiples +---+--+--+")
print("Mean --> PROMEDIO, sum --> SUMA, ")
print("max --> MAXIMO, min --> MINIMO")
resultado_agregado = agrupado['Horas_Capacitacion'].agg(['mean', 'sum', 'max', 'min'])
print(resultado_agregado)
print("-----------+ Agrupacion por varias columnas +-----------")
print("Agrega otra columna al DataFrame (Marco de Datos)")
print("Columna 'teams' (Equipo)")
df['Equipo'] = ['A','B','A','B','A','B']
agrupado_multiple = df.groupby(['Departamento', 'Equipo'])['Evaluacion_Desempeno'].mean()
print(agrupado_multiple)