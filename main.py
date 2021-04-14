from Classes import *
from Sel import *
from readfile import *
from Dictionaries import *

localKs = []
localbs = []

K = []
b = array('f')
T = array('f')

print("TRANSFERENCIA DE CALOR EN 1D")

m = mesh()
leerMalla(m)

crearSistemasLocales(m, localKs, localbs)
# showKs(localKs); showbs(localbs)

zeroes(K, m.getSize(SIZES['NODES']))
arrayZeroes(b, m.getSize(SIZES['NODES']))
ensamblaje(m, localKs, localbs, K, b)
# showMatrix(K)
# print("")
# showArray(b)
# print("")


applyNeumann(m, b)
# showArray(b)
# print("NEUMANN\n")

applyDirichlet(m, K, b)
# showMatrix(K)
# print("")
# showArray(b)
# print("Dirichlet\n")

arrayZeroes(T, len(b))

# showArray(T)
# print("")

calculate(K,b,T)

showArray(T)