from matplotlib import pyplot as plt
import numpy as np
from numpy import polynomial as Pol
from scipy import linalg
from scipy import interpolate as itp
# Carga de archivos a travez de numpy! #

A = np.load('f1.npy') #Se carga el archivo f1.npy con la funcion load de numpy
B = np.load('f2.npy') #Se carga el archivo f2.npy con la funcion load de numpy
X = np.arange(start=1,stop=50,step=1) #Funcion indicada por el profesor, comienza en 1, termina en 50 y da paso 1

# Se realiza las funciones a F1 #
A1 = np.polyfit(X, A, 5) # se ajusta un polinomio en base a X y A(F1) (coordenadas, arreglo, grado del polinomio)
F1 = np.poly1d(A1) # Polinomio unidimensional

# Se realiza las funciones a F2 #
B1 = np.polyfit(X, B, 3) # se ajusta un polinomio en base a X y A(F1) (coordenadas,arreglo, grado del polinomio)
F2 = np.poly1d(B1) # Polinomio unidimensional
plt.plot(X, A, 'o', color='blue') #se ingresan los puntos y su respectivo color para ser representados en el grafico que corresponden a F1
plt.plot(X,F1(X), color='black') #se ingresa la linea que graficara correspondiente a F1
plt.plot(X, B, 'o', color='orange')#se ingresan los puntos y su respectivo color para ser representados en el grafico que corresponden a F2
plt.plot(X, F2(X), color='black') #se ingresa la linea que graficara correspondiente a F2
plt.show()