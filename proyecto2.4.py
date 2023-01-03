from matplotlib import pyplot as plt
import numpy as np
from numpy import polynomial as p
import scipy
from scipy import signal
import cv2

# Se Carga el archivo .npy #
x = np.load('signal.npy')

# Se aplican funciones #
A = scipy.signal.wiener(x, mysize=None, noise=None) # Se aplica el filtro wiener a la matriz x con valores predeterminados
B = scipy.signal.medfilt(x, kernel_size=None) #Se aplica filtro a la matriz x, y se le asigna una dimension

# Funciones para graficar #
plt.xlim([0,100])
plt.ylim([-1.5,1.5])
plt.plot(x, lw=1, label='original')
plt.plot(A, lw=1, label='wiener Filter')
plt.plot(B, lw=1, label='median Filter')
plt.legend(loc=2)
plt.show()
