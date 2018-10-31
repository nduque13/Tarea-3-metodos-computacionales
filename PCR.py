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
    guardavar = unalinea.split(',') 
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

        guardacovas = cova(N[:,i], N[:,j])

        matrix[i,j] = guardacovas
###Imprime el resultado propio d ela matriz de covarianza y el tesultaro teo

print ("Mi resultado es:------------")
print(matrix)
print("El resultado por paquete de numpy es:---------------")
print( np.cov(N.T))


###El siguiente paso es calcular los auto vectores y los auto valores, para lo que crea dos variables llamadas Autovectores y Autovalores y utiliza el paquete eig de numpy para calcularlos.

Autovalores,Autovectores = np.linalg.eig(matrix)



#Utiliza un recorrido para saber a que autovalor corresponde cada autovector 


for k in range(Fil):
    #Busca cada autovalor en las Filas y lo asocia a cada autovector presente



    print( " El autovalor es: ", Autovalores[k])


    print("y su correspondiente autovector es:", Autovectores[:,k])


#Se ordenan los autovalores y los autovectoresssss con respecto al orden de menor a mayor de los autovalores


Autovectores = Autovectores[:,np.argsort(Autovalores)]


Autovalores = Autovalores[np.argsort(Autovalores)]

###Gracias a la teoria sabemos que con los autovectores dados, se puede saber cuales son los componentes principales del analisis, en este caso habria que ver cuales son los ultimos dos autovectores que representarian los F1 y F2, por lo que los autovectores fueron organizados en orden ascendente, para saber cuales dos son los componentes principales!!! 

##por ende busca los dos ultimos autovectores (mayores), que representarian los componentes principales del analisis

C = Autovectores[:,[-1,-2]]

print("Los componentes principales F1 y F2 del analisis serian:", C)


###incizo de hallar la proyeccion de los datos en el sistema de coordenadas 

###como fue hecho anteriormente con la covarianza, halla las proyecciones utilizando una funcion en este caso llamada proy la cual retorna la proyeccion de ambos vectores involucrados

def proyecta(Vec1,Vec2):

	return Vec1[0]*Vec2[0] + Vec1[1]*Vec2[1]



###como paso siguiente lo mas facil es crear un array que guarde las proyecciones para despues poderlo manejar mas facil, lo crea vacio


Proy = []

# crea un recorrido que recorra sobre la longitud de los numeros para encontrar las proyecciones sobre los dos componentes principales previamente guardados en la variable C
#Las dimensiones totales son de 569, que es lo mismo que poner N[:,0] pero por alguna razon se me esta cayendo el codigo asi, por lo que voy a poner 569
for f in range(569):


    #la primera proyeccion va a ser cada dato contra el componente principal 1 almacenado en la variable C
    primeraproyeccion = proyecta(N[f,:], C[:,0])
  
    #la segunda proyeccion va a ser cada dato contra el componente principal 2 almacenado en la variable C
    segundaproyeccion = proyecta(N[f,:], C[:,1])

    #mete los datos encontrados al array creado anteriormente
    Proy.append([primeraproyeccion,segundaproyeccion])



###ME salia TypeError: list indices must be integers, not tuple, por lo que convierto esa lista en un arreglo con np.array
Proy = np.array(Proy)


###Plotea los datos asignandole las letras B (Benigno) y M(Maligno) para diferenciarlos
plt.figure()


plt.plot(Proy[L =='B',0] , Proy[L =='B',1],'c', Proy[L =='M',0] , Proy[L =='M',1],'v')
plt.xlabel("PC1 primer componente principal")
plt.ylabel("PC2 segundo componente principal")
plt.savefig('DuqueNicolas_PCA.pdf')
	
	
###Imprima un mensaje diciendo si el metodo de PCA es util para hacer esta clasificacion, si
#no sirve o si puede ayudar al diagnostico para ciertos pacientes, argumentando claramente
#su posicion.


print("El metodo si es util para realizar la clasificacion, ya que lo que busca el metodo de PCA es que basado en la correlacion entre varias variables se puede saber cuales de estas tienen la mayor correlacion con las demas, para asi saber si seran buenas predictoras de alguna suposicion o algun modelo, en este caso un diagnostico de cancer maligno o benigno. Si puede ayudar al diagnostico ya que las componentes principales hablarian por el resto de las variables, siendo estas las mas correlacionadas entre si, siendo aptas para el modelo. Como se puede ver en la grafica hecha, los puntos de B y M estan sesgados, por lo que responden a lo que las componentes principales hagan, volviendolas a estas buenas predictoras para el modelo")










