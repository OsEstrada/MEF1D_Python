from Classes import *
from Dictionaries import *
from matrix_math import *
from array import array

""" def showMatrix(K):
    n = len(K[0])
    m = len(K)
    for i in range(n):
        print("[\t", end="")
        for j in range(m):
            print(round(K[i][j],4),end="\t")
        print("]")

def showKs(Ks):
    n = len(Ks)
    for i in range(n):
        print("K del elemento ",i+1,":")
        showMatrix(Ks[i])
        print("********************************")

def showbs(bs):
    n = len(bs)
    for i in range(n):
        print("b del elemento",i+1)
        showArray(bs[i])
        print("*******************************") """

def showArray(b):
    print("",end="[\t")
    n = len(b)
    for i in range(n):
        print(round(b[i],5),end="\t")
    print("]")

def createLocalK(element, m):
    K = []
    row1 = array('f')
    row2 = array('f')
    k = m.getParameter(PARAMETERS['THERMAL_CONDUCTIVITY'])
    l = m.getParameter(PARAMETERS['ELEMENT_LENGHT'])
    row1.append(k/l); row1.append(-k/l)
    row2.append(-k/l); row2.append(k/l)
    K.append(row1); K.append(row2)
    return K

def createLocalB(element, m):
    b = array('f')
    Q = m.getParameter(PARAMETERS['HEAT_SOURCE'])
    l = m.getParameter(PARAMETERS['ELEMENT_LENGHT'])
    b.append(Q*l/2); b.append(Q*l/2)
    return b

def crearSistemasLocales(m, localKs, localbs):
    for i in range(m.getSize(SIZES['ELEMENTS'])):
        localKs.append(createLocalK(i, m))
        localbs.append(createLocalB(i, m))

def assemblyK(e, localK, K):
    index1 = e.getNode1()-1
    index2 = e.getNode2()-1
    K[index1][index1] += localK[0][0]
    K[index1][index2] += localK[0][1]
    K[index2][index1] += localK[1][0]
    K[index2][index2] += localK[1][1]

def assemblyb(e, localb, b):
    index1 = e.getNode1()-1
    index2 = e.getNode2()-1
    b[index1] += localb[0]
    b[index2] += localb[1]

def ensamblaje(m, localKs, localbs, K, b):
    for i in range(m.getSize(SIZES['ELEMENTS'])):
        e = m.getElement(i)
        assemblyK(e, localKs[i], K)
        assemblyb(e, localbs[i], b)

def applyNeumann(m, b):
    for i in range(m.getSize(SIZES['NEUMANN'])):
        c = m.getCondition(i, SIZES['NEUMANN'])
        b[c.getNode1()-1] += c.getValue()

def applyDirichlet(m, K, b):
    for i in range(m.getSize(SIZES['DIRICHLET'])):
        c = m.getCondition(i, SIZES['DIRICHLET'])
        index = c.getNode1() - 1
        del K[index]
        b.pop(index)
        s = len(K)
        for i in range(s):
            cell = K[i][index]
            K[i].pop(index)
            b[i] += -1*c.getValue()*cell

def calculate(K, b, T):
    Kinv = []
    inverseMatrix(K, Kinv)
    productMatrixVector(Kinv, b, T)

