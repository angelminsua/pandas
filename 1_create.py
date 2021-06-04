# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 12:45:16 2021

@author: amontinsua
"""


import numpy as np
import pandas as pd


"""
    SERIES
"""
#Creating Series variables by passing a list of values, letting pandas create a default integer index
s1 = pd.Series([1, 2, 3, np.nan, 4, 5])
print("s1=", s1)
print("s1.describe:", s1.describe())

s2 = pd.Series([6, 7, 8, 9, 10, np.nan])
print("s2=", s2)
print("s2.describe:", s2.describe())

s3 = pd.Series([
  np.datetime64("2001-01-01"),
  np.datetime64("2002-01-01"),
  np.datetime64("2010-01-01"),
  np.datetime64("2010-01-01"),
  np.datetime64("2011-01-01"),
  np.datetime64("2012-01-01")
])

print("s3=", s3)
print("s3.describe:", s3.describe())



"""
    DATAFRAMES
"""

df = pd.DataFrame(
    {
    "A": 1.0,
    "B": pd.Timestamp("20130102"), #en la proxima columna hago lo mismo pero con otra funcion
    "B2":pd.date_range("20130101", periods=4),#hay q poner 4 para q coincida con la longitud de las otras columnas donde especifico colecciones de 4 elementos
    "C": pd.Series(1, index=list(range(4)), dtype="float32"),
    "D": np.array([3] * 4, dtype="int32"),
    "E": pd.Categorical(["test", "train", "test", "train"]),
    "F": "foo",
    }
  )


print("df=", df.head(10))
print("columnas del dataframe=", df.columns)
print("indice del dataframe=", df.index)
print("tipos del dataframe=", df.dtypes)
print("df.describe:", df.describe())
print("df.describe all:", df.describe(include='all'))
df_transposed = df.T
print("df_transposed=", df_transposed)

array_from_dataframe = df.to_numpy() #crea un array donde cada elemento es una lista con los elementos de la fila i del dataframe
print("array_from_dataframe=", array_from_dataframe)


#Creating a DataFrame by passing a NumPy array, with a datetime index and labeled columns:
dates1 = pd.date_range("20130101", periods=12)
print("dates1=", dates1)


#Creating a DataFrame by passing a NumPy array, with a datetime index and labeled columns:
dates2 = pd.date_range("201301011212", periods=12)
print("dates2=", dates2)
#np.random.randn(12, 4): Return a sample (or samples) from the “standard normal”. 12: number of rows. 4: number of columns
df = pd.DataFrame(np.random.randn(12, 4), index=dates1, columns=list("ABCD"))
print("df=", df)

