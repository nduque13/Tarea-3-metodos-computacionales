##Comienza el punto 4 de la tarea 3 de metodos computacionales Fourier en 2d


###IMPORTA LIBRERIAS NECESARIAS incluyendo la lectura de imagenes de matplotlib (imread)


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
from scipy.fftpack import fft, fftfreq, ifft, fft2, ifft2


# Almacene la imagen arbol.png en una arreglo de numpy

miarbolpapa = imread('arbol.png')


#Usando los paquetes de scipy, realice la transformada de Fourier de la imagen. Eligiendo
#una escala apropiada, haga una grafica de dicha transformada y guardela sin mostrarla en
#ApellidoNombre_FT2D.pdf.

##Realiza la transformada en 2-D utilizando fft

transforma = fft2(miarbolpapa)
##plotea la transformada que acaba de realizar

plt.figure()
#utiliza el paquete imshow para leer la imagen


plt.imshow(np.abs(transforma))

plt.xlabel('X')
plt.ylabel('Y')
plt.savefig('DuqueNicolas_FT2D.pdf')

##se determina que un filtro bueno es alrededor de 3450 o 3400 o 3500, alguno de esos, por lo que en vez de buscar esa amplitud con un for, se utiliza la funcion de numpy np.where para que busque las amplitudes mayores a 3500 y las elimina.
mayoresque3400 = np.where(transforma > 3400)



transforma[mayoresque3400] = 0

##Grafique la transformada de Fourier despues del proceso de filtrado, esta vez en escala
#LogNorm y guarde dicha grafica sin mostrarla en ApellidoNombre_FT2D_filtrada.pdf.

plt.figure()


#tiene que usar escala logaritmica entonces para eso utiliza

escalalog = np.log(np.abs(transforma))
plt.imshow(escalalog)

plt.grid()
plt.xlabel('X')
plt.ylabel('Y')
plt.colorbar()
plt.savefig('DuqueNicolas_FT2D_filtrada.pdf')




