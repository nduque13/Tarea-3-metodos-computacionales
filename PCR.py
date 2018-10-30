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

#Se aseguran que sean arreglos con np.array

L = np.array(L)
N = np.array(N)


N = N.astype(float)




#Empiueza a calcular la covarianza definiendo las columnas y la filas para nuestra matriz

#Datos
Col = np.size(N,0) 

#Variables
Fil = np.size(N,1)


#Como la formula de la covarianza estipula que es la sumatoria de (X-Xprom)*(Y-Yprom)/N-1 Siendo N el numero total de datos y siendo X y Y variables
#Se empieza por calcular el promedio de las variables dadas 

##se crea una funcion que calcule los promedios, debido a la extension de los datos no se hace a mano

def cova(A,B):
    #Calcula los promedios para las variables de interes, por eso entran A,B


    Col = len(A)

    # Promedios
	Meanb = np.mean(B)

    Meana = np.mean(A)

   

#Define lo que va a calcular la funcion de covarianza, debido a la extension de los datos

    return np.sum( (A-Meana)*(B-Meanb) )/(Col-1)

#Crea una matriz que almacene ceros hasta que los datos de la covarianza sean introducidos con las dimensiones de Fil

matrix = np.zeros((Fil,Fil))
#Crea dos recorridos como haciamos en el ejercicio de matrices para la tarea 2 que recorra filas y columnas
for i in range(Fil):
    for j in range(Fil):
        # i,j son recorridos en las variables (columnas)

        ij = cova(N[:,i], N[:,j])

        matrix[i,j] = ij

print(matrix, '\n'*3, np.cov(N.T))




