##Comienza el punto 2 de la tarea 3 de metodos computacionales PCA-PCR

###IMPORTA LIBRERIAS NECESARIAS
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import eig

#Importa los datos de WDBC.dat con genfromtxt
datos = np.genfromtxt('WDBC.dat', dtype='str')



#Creo dos listas vacias que me almacenen los numeros y las letras, debido a la presencia de el campo con la letra M o B en los datos .dat


L = []




N = []

#Crea un recorrido para buscar letras y numeros dentro de los datos
for unalinea in datos:

# Como los datos estan separados por comas 
    guardavar = unalinea.split(sep=',') 
    #Guarda los datos en el arreglo N, y la letras en el arreglo L

    N.append(guardavar[2:])


    L.append(guardavar[1])

