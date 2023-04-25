# -*- coding: utf-8 -*-
"""Ejercicio5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LhvBicAUXKzPzvqTg0NAJEuumn-pNK_2

Importo mi base de datos previamente modificada en Weka con 20 filas aleatorias y 4 columnas
"""

import pandas as pd
df = pd.read_csv('/content/drive/MyDrive/Datasets/winequality-red-random-4col.csv')

!pip install scikit-learn==1.2.2

df

df.info()

"""Separo la base de datos en dos objetos: X para explicar y Y como la explicada (objetivo)"""

X = df.iloc[:,0:3]

Y = df.iloc[:,3]

X

Y

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
print(X_test)
print(X_train)

"""Para hacer el árbol note que uso los 20 datos pues 16 me parece poco y prefiero usar todo como en sus ejemplos. Aunque podria usar 16 usando X_train y Y_train"""

from sklearn import tree
clasificador = tree.DecisionTreeClassifier(criterion='entropy', splitter='best')
resultados = clasificador.fit(X, Y)

"""Instalo matplotlib para graficar el árbol  """

!pip install matplotlib

"""En el árbol X[0]=fixed acidity 	X[1]=citric acid 	X[2]=pH 

Value es el numero de instancias cuya calidad (quality) es [4,5,6,7] en ese orden.

Samples es el numero de instancias que responden a la pregunta si o no de la cabecera de cada cuadro

Nota: En la pregunta de la cabezera de cuadro  (ej X[0]<=7.4) las instancias que responden si, van a la izquierda, las que responden no van a la derecha
"""

from matplotlib import pyplot as plt
from sklearn import tree
fig = plt.figure(figsize=(25,20))
tree.plot_tree(resultados)
plt.show()