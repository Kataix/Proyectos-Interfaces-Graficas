from matplotlib import pyplot as plt
import numpy as np
from numpy import polynomial as Pol
from scipy import linalg
from scipy import interpolate as itp

# Se cargan los archivos y se separan los dos arreglos que que contiene  #
che = np.load('cheby.npy')
x = che[0]
y = che[1]

# Se trabajan los arreglos para calcular su polinomio#
deg = len(x) - 1
A = Pol.chebyshev.chebvander(x, deg)
c = linalg.solve(A, y)
ecu = Pol.Chebyshev(c)
print (ecu)

# Se Grafica los valores usando el polinomio calculado  anteriormente  #
graf = np.linspace(x.min(), x.max(), 100)
fig, ax = plt.subplots(1, 1, figsize =(12, 4))
ax.scatter (x, y, color= 'red', label="Puntos de informacion")
ax.plot (graf, ecu(graf), 'b', lw=2, label="Chebyshev")
ax.legend (loc=4)
ax.set_xticks(x)
ax.set_ylabel(r"$y$", fontsize = 10)
ax.set_xlabel(r"$x$", fontsize = 10)
plt.show()
