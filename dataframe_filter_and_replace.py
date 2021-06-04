# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 18:19:36 2021

@author: amontinsua
"""

import pandas as pd

#Declarar un DataFrame (vacio)
data = pd.DataFrame(columns=('order', 'family', 'num', 'sequence'))
#Añadir datos al DataFrame
data.loc[len(data)]=['Tymovirales','Alphaflexiviridae',1,'AACGTTAAUGGUGAA'] 
data.loc[len(data)]=['Tymovirales','Alphaflexiviridae',2,'AACGTTAAUGGUGAA']

#Declarar un DataFrame (con datos)
clases = ["clase 1"] * 5 + ["clase 2"] * 5
tipos = ["tipo 1"] * 2 + ["tipo 2"] * 3 + ["tipo 3"] * 2 + ["tipo 4"] * 3
valores = [0,1,2,3,4] + [5,6,7,8,9]
df = pd.DataFrame({"clase": clases, "tipo": tipos, "valor": valores})
#Mostrar los 4 primeros elementos del Dataframe
print(df[:4])
#Acceder al primer registro
primera_fila = df.loc[1] #otra forma:  print(df.iloc[1])

print("primera_fila=", primera_fila)

#Ordenar valores por clase y tipo
print(df.sort_values(by=['clase','tipo'], ascending=[True,False]))

#Reemplazar subcadena para todos los campos de una columna
df['clase'] = df['clase'].replace({' ': ''}, regex=True)
print(df)

#Reemplazar subcadena para todos los campos del dataframe
df = df.replace({' ': ''}, regex=True)
print(df)

#Filtrar por valores de una columna
df2 = df[df['tipo'] == 'tipo1']
print(df2)

#Filtrar por columnas concretas del dataframe
df2 = df.filter(items=['clase', 'valor'])
print(df2)

#Filtar por valores de una columna que pertenezcan a un conjunto de datos
df2 = df[df['valor'].isin([3,5])]
print(df2)

#Filtar por valores que cumpla una condición
df2 = df[df['valor'] > 5]
print(df2)