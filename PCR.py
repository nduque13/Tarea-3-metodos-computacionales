##Comienza el punto 2 de la tarea 3 de metodos computacionales PCA-PCR

###IMPORTA LIBRERIAS NECESARIAS
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import eig

#Importa los datos de WDBC.dat con genfromtxt
datos = np.genfromtxt('WDBC.dat', dtype='str')
