# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 11:37:41 2019

@author: MNO
"""

import pandas as pd
# Leemos el csv de paradas, que es la tabla en la que se identifican los códigos y nombres de las paradas. Nos quedamos solo con las tres columnas que nos interesan (Id, NomPar, Largo)
df_paradas=pd.read_csv('PARADAS.csv', sep=';', usecols=['Id', 'NomPar', 'Largo'])


def acentosetc(a):
# Esta función sirve para quitar todos los errores de conversión de acentos y eñes de la BD CTC
    a=str(a)
    a=a.replace('<f3>', 'ó')
    a=a.replace('<e9>', 'é')
    a=a.replace('<f1>', 'ñ')
    a=a.replace('<ed>', 'í')
    a=a.replace('<U+00AA>', 'ª')
    a=a.replace('<fa>', 'ú')
    a=a.replace('<e1>', 'á')
    a=a.replace('<U+00BA>', 'º')
    return(a)

# Aplicamos la función a las comlumnas de nombre de parada y de nombre largo de parada para que no aparezcan errores
df_paradas['NomPar']=df_paradas['NomPar'].apply(acentosetc)
df_paradas['Largo']=df_paradas['Largo'].apply(acentosetc)

#with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
#    print(df_paradas)
print('Tabla de paradas', '------------------------------------------------------------------')
print(df_paradas.columns)
# A continuación establecemos la forma de impresión sin límite de filas ni de columnas, para poder hacernos una idea clara de las tablas
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(df_paradas)

# Leemos las primeras 100000 filas de la tabla de viajes de conductores 
df_vcond=pd.read_csv('VCOND.csv', sep=';', low_memory=False, nrows=100000)
#print('Tabla vcond', '------------------------------------------------------------------')
#print(df_vcond.columns)
#with pd.option_context('display.max_columns', None):  # more options can be specified also
#    print(df_vcond)

#print(df_vcond.columns)

# Leemos las primeras 100000 filas de la tabla de paradas de viaje
df_pviaje=pd.read_csv('PVIAJE_entero.csv', sep=',', nrows=100000)
#print('Tabla pviaje', '------------------------------------------------------------------')
#print(df_pviaje.columns)
#with pd.option_context('display.max_columns', None):  # more options can be specified also
#    print(df_pviaje)

#print(df_pviaje.columns)

# Combinamos las tablas de viajes de conductores y paradas de viaje con un left join
# Con ello tenemos la información de la hora de paso por cada parada de cada uno de los viajes
df_combined=pd.merge(df_vcond, df_pviaje, how='left', left_on='Id', right_on='IdVCond')

# Definimos las columnas con las que nos queremos quedar de la tabla combinada
df_combined=df_combined[['Id_x', 'Fecha', 'Cond', 'Bus', 'Linea',
       'Sentiida', 'Servi', 'HSal', 'HLle', 'Pack', 'IdVCond', 'Hora', 'IdPar']]

# Combinamos la tabla combinada anterior con la de paradas, mediante un left join
# Con ello conseguimos tener el nombre de cada parada y nombre largo al lado de su código en la tabla combinada
df_comb_stname=pd.merge(df_combined, df_paradas, how='left', left_on='IdPar', right_on='Id')

# Definimos las columnas con las que nos queremos quedar de la tabla combinada
df_comb_stname=df_comb_stname[['Id_x', 'Fecha', 'Cond', 'Bus', 'Linea', 'Sentiida', 'Servi', 'HSal',
       'HLle', 'Pack', 'IdVCond', 'Hora', 'IdPar', 'NomPar', 'Largo']]

# Eliminamos las filas que tienen NaN en la columna IdPar
df_comb_stname=df_comb_stname.dropna(subset=['IdPar'])

df_comb_stname=df_comb_stname.astype({'IdPar': 'int32', 'IdVCond': 'int32'})

print('Tabla combined with stop names', '------------------------------------------------------------------')
print(df_comb_stname.columns)
with pd.option_context('display.max_columns', None):  # more options can be specified also
    print(df_comb_stname)

#print(df_comb_stname['Largo'].where(df_comb_stname['Linea']==700).where(df_comb_stname['Sentiida']==True).dropna().unique())

# De la tabla combinada con hora de paso por paradas y nombres de paradas seleccionamos las filas correspondientes a la línea 7 (700)
# y a la parada 186 con viaje en sentido ida. Cuidado con el dropna que creo que estoy eliminando todas las líneas con NaN en algún campo. 
# Se puede cambiar a la sintaxis de antes indiándole que sea en la fila de IdPar
df_186=df_comb_stname.where(df_comb_stname['Linea']==700).where(df_comb_stname['IdPar']==186).where(df_comb_stname['Sentiida']==True).dropna()
print('df_186', '-------------------------------------------------------------')
print(df_186)
print(df_186.columns)

# Hago lo mismo pero en este caso con la parada 92. Cuidado de nuevo con lo de dropna()
df_92=df_comb_stname.where(df_comb_stname['Linea']==700).where(df_comb_stname['IdPar']==92).where(df_comb_stname['Sentiida']==True).dropna()
print('df_92', '-------------------------------------------------------------')
print(df_92)
print(df_92.columns)

# Aquí combino las tablas de las dos paradas, con un join left, revisar otra vez lo del dropna
# Se han seleccionado las columnas de interés y elminado las duplicaciones de datos.
df_186_92=pd.merge(df_186, df_92, how='left', left_on='IdVCond', right_on='IdVCond').dropna()
df_186_92=df_186_92[['Id_x_x', 'Fecha_x', 'Cond_x', 'Bus_x', 'Linea_x', 'Sentiida_x',
       'Servi_x', 'HSal_x', 'HLle_x', 'Pack_x', 'IdVCond', 'Hora_x', 'IdPar_x',
       'NomPar_x', 'Largo_x', 'Id_x_y', 'Fecha_y', 'Cond_y', 'Bus_y',
       'Hora_y', 'IdPar_y', 'NomPar_y', 'Largo_y']]

# Generar una nueva columna con el tiempo de recorrido entre las dos paradas. Por ahora no funciona porque las columnas de Hora_x y Hora_y tienen formato de string
#df_186_92['Tiempo']=df_186_92['Hora_x']-df_186_92['Hora_y']
print(df_186_92.columns)
print('df_186_92', '------------------------------------------------------------------')
with pd.option_context('display.max_columns', None):  # more options can be specified also
    print(df_186_92)
#

# Guardamos la tabla combinada a un csv
df_186_92.to_csv('df_186_92.csv')

