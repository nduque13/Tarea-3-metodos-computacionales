##Comienza el punto 4 de la tarea 3 de metodos computacionales Fourier en 2d


###IMPORTA LIBRERIAS NECESARIAS incluyendo la lectura de imagenes de matplotlib (imread)


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
from scipy import fft, fftfreq, fft2, ifft, ifft2


# Almacene la imagen arbol.png en una arreglo de numpy

miarbolpapa = imread('arbol.PNG')


#Usando los paquetes de scipy, realice la transformada de Fourier de la imagen. Eligiendo
#una escala apropiada, haga una gráfica de dicha transformada y guárdela sin mostrarla en
#ApellidoNombre_FT2D.pdf.

##Realiza la transformada en 2-D utilizando fft

transforma = np.fft.fft2(miarbolpapa)
##plotea la transformada que acaba de realizar

plt.figure()
#utiliza el paquete imshow para leer la imagen


plt.imshow(np.abs(transforma))

plt.xlabel('X')
plt.ylabel('Y')
fig.savefig('DuqueNicolas_FT2D.pdf')









