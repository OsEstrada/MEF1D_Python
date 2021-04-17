from Classes import *
from Dictionaries import *
from matrix_math import *
from array import array

#Esta funcion muestra la matriz
def showMatrix(K):
    n = len(K[0])
    m = len(K)
    for i in range(n):
        print("[\t", end="")
        for j in range(m):
            print(round(K[i][j],4),end="\t")
        print("]")
    print("")

#Esta funcion se encarga de mostrar las Ks locales
def showKs(Ks):
    n = len(Ks)
    for i in range(n):
        print("K del elemento ",i+1,":")
        showMatrix(Ks[i])
        print("-------------------------------")
    print("")

#Esta funcion se encarga de mostrar las bs locales
def showbs(bs):
    n = len(bs)
    for i in range(n):
        print("b del elemento",i+1)
        showArray(bs[i])
        print("-------------------------------")
    print("")

#Esta funcion muestra los valores de una lista o arreglo con un formato especifico
def showArray(b):
    print("",end="[\t")
    n = len(b)
    for i in range(n):
        print(round(b[i],5),end="\t")
    print("]", end ="\n")

#Esta funcion recibe la malla y devuelve la matriz K local
def createLocalK(m):
    K = []
    row1 = array('f')
    row2 = array('f')
    #Obtiene los valores de k y l (se asume l como una variable de entrada) y que la malla es regular
    k = m.getParameter(PARAMETERS['THERMAL_CONDUCTIVITY'])
    l = m.getParameter(PARAMETERS['ELEMENT_LENGHT'])
    #Se asignan los valores a las celdas de la matriz = (k/L)[{1,-1}{-1,1}] los cuales se agregan a la matriz
    row1.append(k/l); row1.append(-k/l)
    row2.append(-k/l); row2.append(k/l)
    K.append(row1); K.append(row2)
    #Se retorna la matriz K
    return K

#Esta funcion recibe la malla y devuelve el vector b local
def createLocalB(m):
    b = array('f') #Se inicializa la matriz de tipo float
    #Obtiene el valor de Q y el valor de l
    Q = m.getParameter(PARAMETERS['HEAT_SOURCE'])
    l = m.getParameter(PARAMETERS['ELEMENT_LENGHT'])
    #Se agregan los valores al arreglo = [Q*(l/2),Q*(l/2)]
    b.append(Q*l/2); b.append(Q*l/2)
    return b

#Esta funcion crea los sitemas locales (K y b) y almacena los datos en sus respectivas listas
def crearSistemasLocales(m, localKs, localbs):
    for i in range(m.getSize(SIZES['ELEMENTS'])):
        localKs.append(createLocalK(m))
        localbs.append(createLocalB(m))

#Esta funcion realiza el ensamblaje del arreglo b global, recibe el elemento actual, el arreglo b local
#y el arreglo b glocal en el cual se realizara el ensablaje
def assemblyb(e, localb, b):
    #La numeracion de los nodos inicia en 1, pero los indices del arreglo inician en 0, asi que se resta 1
    #al valor del index.
    index1 = e.getNode1()-1
    index2 = e.getNode2()-1
    b[index1] += localb[0]
    b[index2] += localb[1]

#Esta funcion realiza el ensamblaje de la matriz K global, recibe el elemento actual, la matriz K local
# y la matriz K global en la cual se realizara el ensamblaje
def assemblyK(e, localK, K):
    #La numeracion de los nodos inicia en 1, pero los indices del arreglo inician en 0, asi que se resta 1
    #al valor del index.
    index1 = e.getNode1()-1
    index2 = e.getNode2()-1
    #Se asignan los elementos en las celdas de la submatriz.
    K[index1][index1] += localK[0][0]
    K[index1][index2] += localK[0][1]
    K[index2][index1] += localK[1][0]
    K[index2][index2] += localK[1][1]


#Se realiza el ensamblaje de los sistemas locales K y B utilizando las funciones assemblyK y assemblyb
def ensamblaje(m, localKs, localbs, K, b):
    for i in range(m.getSize(SIZES['ELEMENTS'])):
        e = m.getElement(i)
        assemblyK(e, localKs[i], K)
        assemblyb(e, localbs[i], b)

#Aplica la condicion de Neumann en el arreglo b global
def applyNeumann(m, b):
    for i in range(m.getSize(SIZES['NEUMANN'])):
        c = m.getCondition(i, SIZES['NEUMANN'])
        b[c.getNode1()-1] += c.getValue()

#Aplica la condicion de dirichlet al sistema de ecuaciones matriciales. Recibe la malla, la matriz K global y
#el arreglo b global
def applyDirichlet(m, K, b):
    #Se recorre el arreglo que almacena las condiciones de Dirichlet
    for i in range(m.getSize(SIZES['DIRICHLET'])):
        #Se crea una variable que almacena la condicion de dirichlet almacenada en el indice i
        c = m.getCondition(i, SIZES['DIRICHLET'])
        #Se almacena el indice del nodo actual.
        index = c.getNode1() - 1
        #Se elimina la primera ecuacion del sistema (es decir la fila de la matriz en que se encuentra el nodo 
        # y el dato del arreglo b donde se encuentra el nodo )
        del K[index]
        b.pop(index)
        s = len(K)
        for i in range(s):
            cell = K[i][index]
            K[i].pop(index)
            b[i] += -1*c.getValue()*cell

#Esta funcion calcula la solucion del sistema de ecuaciones y lo almacena en el arreglo T
def calculate(K, b, T):
    Kinv = [] #Se crea la variable que almacenara la matriz inversa
    inverseMatrix(K, Kinv) #Se invierte la matriz K global y se almacena en la matriz Kinv
    productMatrixVector(Kinv, b, T) #Se multiplica Kinv por el arreglo b, y su resultado se almacena en el arreglo T

