import numpy as np
from matplotlib import pyplot as plt
from scipy import signal as sig
# Funciones entregadas por el prof. #
t = np.linspace(0,5,100)
x = t + np.random.normal(size = 100)

# Se Separan las tendencias de la señal #
tendenciax = sig.detrend(x)
# Se Grafica #
plt.xlim([0,6])
plt.plot(t,x, lw=1, color='red', label='Tendencia')
plt.plot(t,tendenciax, lw=1, color='blue', label='Sin su Tendencia')
plt.legend(loc=2)
plt.show()
