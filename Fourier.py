##Comienza el tercer punto de la tercera tarea de Metodos Computacionales, transformada de fourier

##importa los paquetes necesarios

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

from scipy.fftpack import fft, fftfreq


##Almacena los datos de senal.dat y de incompletos.dat

lasenal = np.genfromtxt('signal.dat')
losincompletos = np.genfromtxt('incompletos.dat')

##Como en signal.dat hay entradas que no son numeros, se aplica slicing para que no afecten el ejercicio

lasenal = lasenal[:,[0,-1]]


##Hace una grafica de senal y la guarda sin mostrarla como es indicado

plt.figure()
plt.plot(lasenal)
plt.xlabel("senal")
plt.ylabel("")
plt.savefig("DuqueNicolas_signal.pdf")

###Hace implementacion propia de la transformada de fourier de los datos
lensen = len(lasenal)
print (lensen)

N = lensen

for n in range(N):
	suma = 0.0
	for i in range(N):
		suma +=  lasenal[i]*(np.exp(-1j*2*np.pi*i*(n/N)))
	print(suma)
suma = np.array(suma)
print("La transformada de fourier es:", suma)

prueba = fft(lasenal)
print("Teorico es------------------")
print(prueba)


##grafica la transformada de fourier encontrada por implementacion propia y la transformada de fourier con paquete LO HAGO POR SABER COMO SON LAS GRAFICAS utiliza el paquete de fftfreq

dt = 1.0/N
freqsenal = fftfreq(N,dt)

plt.plot(freqsenal,prueba)
plt.show()



