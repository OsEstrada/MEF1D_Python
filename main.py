from Classes import *
from Sel import *
from readfile import *
from Dictionaries import *

#Se instancias las listas/Matrices a utilizar
localKs = []
localbs = []

K = []
b = array('f')
T = array('f')

print("TRANSFERENCIA DE CALOR EN 1D")

#Se crea un objeto de tipo mesh
m = mesh()
#Se leen los elementos del archivo de texto y se almacenan en sus correspondientes variables dentro de la malla m
leerMalla(m)
#Se crean los sistemas locales en base a la informacion leida y se muestra
crearSistemasLocales(m, localKs, localbs)
showKs(localKs); showbs(localbs)
#Se incializan las matrices con ceros y luego se ejecuta el ensamblaje
zeroes(K, m.getSize(SIZES['NODES']))
arrayZeroes(b, m.getSize(SIZES['NODES']))
ensamblaje(m, localKs, localbs, K, b)

# showMatrix(K)
# print("")
# showArray(b)
# print("")

#Se aplican las condicones de Neumann al arreglo b
applyNeumann(m, b)
# showArray(b)
# print("NEUMANN\n")

#Se aplican las condiciones de Dirichlet al sistema de ecuaciones
applyDirichlet(m, K, b)
# showMatrix(K)
# print("")
# showArray(b)
# print("Dirichlet\n")

#Se inicializa el arreglo T en ceros, con una longitid igual a la del arreglo b
arrayZeroes(T, len(b))

# showArray(T)
# print("")

#Se calcula el resultado del sistema de ecuaciones Kb = T
calculate(K,b,T)

#Se muestra el resultado final del modelo
showArray(T)