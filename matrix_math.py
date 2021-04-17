from array import array

#Funcion que llena una matriz de tipo float con dimensiones nxn de ceros
def zeroes(Matrix, n):
    for i in range(n):
        Matrix.insert(i,array('f', (0.0 for i in range(n))))

#Funcion que llena un arreglo de tamaño n con ceros
def arrayZeroes(Array, n):
    for i in range(n):
        Array.append(0.0)

#Funcion que copia los elementos de una matriz A a otra matriz B
def copyMatrix(A, B):
    zeroes(B, len(A))
    #Se almacenan el numero de filas(n) y el numero de columnas(m) y se guardan en una variable para evitar su repetida ejecucion
    n = len(A)
    m = len(A[0])
    #Ya que la matriz es realmente una lista de arreglos, para copiarlo debo recorrer cada una de sus celdas y almacenarlas en la matriz
    #de destino, si se copia unicamente las filas, realmente estaria almacenando una referencia y no los valores en bruto.
    for i in range(n):
        for j in range(m):
            B[i][j] = A[i][j]

#Esta funcion realiza el producto de una Matrix M por un arreglo o vector V
def productMatrixVector(M, V, R):
    n = len(M)
    for i in range(n):
        m = len(V)
        cell = 0.0
        for j in range(m):
            cell += M[i][j] * V[j]
        R[i] += cell

#Esta funcion realiza el producto de un numero real por cada uno de los elementos almacenados en una matriz
def productRealMatrix(real, M, R):
    n = len(M)
    m = len(M[0])
    zeroes(R, n)
    for i in range(n):
        for j in range(m):
            R[i][j] = real * M[i][j]

#Esta funcion calcula el menor de una matriz (elimina la fila y columna dada una celda)
def getMinor(M, i, j):
    M.pop(i)
    n = len(M)
    for k in range(0,n):
        M[k].pop(j)

#Esta funcion calcula el determinante de una matriz
def determinant(M):
    #Si la matriz tiene solo una fila, se devuelve dicho valor como determinante
    if len(M) == 1:
        return M[0][0]
    else:
        det = 0.0
        for i in range(0,len(M[0])):
            minor = []
            copyMatrix(M, minor)
            getMinor(minor, 0, i)
            det = det + ((-1)**i)*M[0][i]*determinant(minor)
        return det

#Calcula la matriz de cofactores
def cofactors(M, Cof):
    n = len(M)
    m = len(M[0])
    zeroes(Cof, n)
    for i in range(n):
        for j in range(m):
            #Se crea una matriz la cual almacenara el menor de la celda actual
            minor = []
            copyMatrix(M, minor)
            getMinor(minor,i,j)
            #Se calcula el cofactor y se alamcena en la matriz de cofactores en la celda i,j
            Cof[i][j] = ((-1)**(i+j))*determinant(minor)

#Esta funcion calcula la transpuesta de una matriz, y almacena el resultado en la matriz T
def transpose(M, T):
    n = len(M)
    m = len(M[0])
    zeroes(T, n)
    for i in range(n):
        for j in range(m):
            T[j][i] = M[i][j]

#Esta funcion calcula la inversa de una matriz utilizando el metodo de la adjunta
def inverseMatrix(M, Minv):
    det = determinant(M)
    #Se verifica el determinante de la matriz, puesto que si una matriz tiene un determinante 0, no posee inversa
    if det == 0:
        print("exit")
        exit()
    else:
        #La inversa por el metodo de la adjunta consiste en calcular la matriz adjunta (una matriz de cofactores transpuesta),
        #y a cada elemento multiplicarlo por 1/determinante de la matriz original
        Cof = []
        Adj = []
        cofactors(M,Cof)
        transpose(Cof,Adj)
        productRealMatrix(1/det, Adj, Minv)
