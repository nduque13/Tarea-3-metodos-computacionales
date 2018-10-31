##Comienza el punto 4 de la tarea 3 de metodos computacionales Fourier en 2d


###IMPORTA LIBRERIAS NECESARIAS incluyendo la lectura de imagenes de matplotlib (imread)


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
from scipy.fftpack import fft, fftfreq, ifft, fft2, ifft2


# Almacene la imagen arbol.png en una arreglo de numpy

miarbolpapa = imread('arbol.PNG')


#Usando los paquetes de scipy, realice la transformada de Fourier de la imagen. Eligiendo
#una escala apropiada, haga una grafica de dicha transformada y guardela sin mostrarla en
#ApellidoNombre_FT2D.pdf.

##Realiza la transformada en 2-D utilizando fft

transforma = np.fft.fft2(miarbolpapa)
##plotea la transformada que acaba de realizar

plt.figure()
#utiliza el paquete imshow para leer la imagen


plt.imshow(np.abs(transforma))

plt.xlabel('X')
plt.ylabel('Y')
plt.savefig('DuqueNicolas_FT2D.pdf')

##se determina que un filtro bueno es alrededor de 3450 o 3400 o 3500, alguno de esos, por lo que en vez de buscar esa amplitud con un for, se utiliza la funcion de numpy np.where para que busque las amplitudes mayores a 3500 y las elimina.


#busca en donde hay amplitudes mayores a 3500 y las elimina

mayoresque3500 = np.where(transforma > 3500)



transforma[mayoresque3500] = 0
scalita = np.log(np.abs(transforma))
#tiene que usar escala logaritmica entonces para eso utiliza




##Grafique la transformada de Fourier despues del proceso de filtrado, esta vez en escala
#LogNorm y guarde dicha grafica sin mostrarla en ApellidoNombre_FT2D_filtrada.pdf.

plt.figure()

plt.imshow(scalita)
plt.grid()
plt.xlabel('X')
plt.ylabel('Y')
plt.colorbar()

plt.savefig('DuqueNicolas_FT2D_filtrada.pdf')


#Haga la transformada de Fourier inversa y grafique la imagen filtrada. Verifique que su
#filtro elimina el ruido periodico y guarde dicha imagen sin mostrarla en
#ApellidoNombre_Imagen_filtrada.pdf.





