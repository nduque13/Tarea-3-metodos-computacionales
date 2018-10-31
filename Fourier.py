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

lasenal = lasenal[:, 2]


##Hace una grafica de senal y la guarda sin mostrarla como es indicado

plt.figure()
plt.plot(lasenal)
plt.xlabel("senal")
plt.ylabel("")
plt.savefig("DuqueNicolas_signal.pdf")

###Hace implementacion propia de la transformada de fourier de los datos
lensen = len(lasenal)


N = lensen


def fourier(lasenal):
	fourier = []
	for n in range(N):
		suma = 0.0
		for i in range(N):
			suma +=  (lasenal[i])*(np.exp(-1j*2*np.pi*i*(n/N)))
			fourier.append(suma)
	return fourier
porfinfourier = fourier(lasenal)
print(porfinfourier)
print("La transformada de fourier es:", porfinfourier)



##grafica la transformada de fourier encontrada por implementacion propia y la transformada de fourier con paquete LO HAGO POR SABER COMO SON LAS GRAFICAS utiliza el paquete de fftfreq NO ME FUNCIONA Y ME GRAFICA LO QUE NO ES, por lo que dejo comentado como me daria con mi implementacion y la grafico con los paquetes de scipy

longfouri = len(porfinfourier) 
NN = longfouri
dt = 1.0/NN
freqsenal = fftfreq(NN,dt)

#plt.plot(freqsenal,porfinfourier)
#plt.show()
DT = 1.0/N
trans = fft(lasenal)
freqnueva = fftfreq(N,DT)

##OJOOO esto es con paquetes, si quiere ver la grafica con mis valores descomentela, da asquerosa.

plt.plot(freqnueva, abs(trans))

plt.xlim(-100,100)

plt.savefig("DuqueNicolas_TF.pdf")



