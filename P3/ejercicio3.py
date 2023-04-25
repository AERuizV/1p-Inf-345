# -*- coding: utf-8 -*-
"""Ejercicio3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KbU5vo-KN9ic01AUf5fiemRSycyE-UFr
"""

import pandas as pd
import numpy as np
df = pd.read_csv('/content/drive/MyDrive/Datasets/winequality-red.csv')
!pip install scikit-learn==1.2.2

df.head()

"""He importado con pandas, pero para usar scikit learn debo usar un arreglo de Numpy"""

A = np.array(df)

"""Estandarizacion, es para ver cuan lejos los datos estan de la media """

from sklearn import preprocessing
tecnica = preprocessing.StandardScaler()
salida = tecnica.fit_transform(A)
print(salida)

"""Normalize, hace un escalado de los datos usando diferentes normas. En este caso la norma del maximo """

from sklearn import preprocessing
tecnica = preprocessing.Normalizer()
salida = tecnica.fit_transform(A, 'norm=max')
print(salida)

"""Binarizer, es para convertir tus datos a binario, los positivos los convierte en 1 y los no positivos en cero"""

from sklearn import preprocessing
tecnica = preprocessing.Binarizer()
salida = tecnica.fit_transform(A)
print(salida)