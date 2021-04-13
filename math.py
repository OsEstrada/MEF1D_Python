from array import array

def zeroes(Matrix, n):
    for i in range(n):
        Matrix.insert(i,array('f', (0.0 for i in range(n))))

def arrayZeroes(Array, n):
    for i in range(n):
        Array[i] = 0.0

def productMatrixVector(M, V):
    n = len(M)
    R = [0.0]*n
    for i in range(n):
        m = len(V)
        cell = 0.0
        for j in range(m):
            cell += M[i][j] * V[j]
        R[i] += cell
    return R

def productRealMatrix(real, M):
    n = len(M)
    m = len(M[0])
    R = []
    zeroes(R, n)
    for i in range(n):
        for j in range(m):
            R[i][j] = real * M[i][j]
    return R

def getMinor(M, i, j):
    del M[i]
    n = len(M)
    for k in range(n):
        M[i].pop(M[i][j])

def determinant(M):
    if len(M) == 1:
        return M[0][0]
    else:
        det = 0.0
        n = len(M[0])
        for i in range(n):
            minor = M.copy()
            getMinor(minor, 0, j)

            det += ((-1)**i)*M[0][i]*determinant(minor)


def cofactors(M):
    Cof = []
    n = len(M)
    m = len(M[0])
    zeroes(Cof, n)
    for i in range(n):
        for j in range(m)
            minor = M.copy()
            getMinor(minor,i,j)
            Cof[i][j] = ((-1)**(i+j))*determinant(minor)
    return Cof

def transpose(M):
    T = []
    zeroes(T)
    n = len(M)
    m = len(M[0])
    for i in range(n):
        for j in range(m):
            T[j][i] = M[i][j]
    return T

def inverse(M):
    det = determinant(M)
    if det == 0:
        exit()
    else:
        Cof = cofactors(M).copy()
        Adj = transpose(Cof).copy()
        Minv = productRealMatrix(1/det, Adj)
        return Minv

# Ma = []
# B = array('f', (i+1 for i in range(5)))
# print("B ", B)

# for i in range(6):
#         Ma.insert(i,array('f', (j+i for j in range(5))))

# for row in Ma:
#     print(row)

# print("\n")

# A = productMatrixVector(Ma, B).copy()
# for row in A:
#     print(row)