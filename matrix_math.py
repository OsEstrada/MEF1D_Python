from array import array

def zeroes(Matrix, n):
    for i in range(n):
        Matrix.insert(i,array('f', (0.0 for i in range(n))))

def arrayZeroes(Array, n):
    for i in range(n):
        Array.append(0.0)

def copyMatrix(A, B):
    zeroes(B, len(A))
    n = len(A)
    m = len(A[0])
    for i in range(n):
        for j in range(m):
            B[i][j] = A[i][j]

def productMatrixVector(M, V, R):
    n = len(M)
    for i in range(n):
        m = len(V)
        cell = 0.0
        for j in range(m):
            cell += M[i][j] * V[j]
        R[i] += cell

def productRealMatrix(real, M, R):
    n = len(M)
    m = len(M[0])
    zeroes(R, n)
    for i in range(n):
        for j in range(m):
            R[i][j] = real * M[i][j]

def getMinor(M, i, j):
    M.pop(i)
    n = len(M)
    # print(len(M[0]), " colums in minor")
    # print(len(M), " rows in minor")
    # print(j, "j value")
    for k in range(0,n):
        M[k].pop(j)

def determinant(M):
    if len(M) == 1:
        return M[0][0]
    else:
        # print("ELSE")
        det = 0.0
        for i in range(0,len(M[0])):
            minor = []
            copyMatrix(M, minor)
            # print(len(minor[0]), " colums in minor")
            # print(len(minor), " rows in minor")
            # print(len(M[0]), " colums in M")
            # print(len(M), " rows in M")
            getMinor(minor, 0, i)
            det = det + ((-1)**i)*M[0][i]*determinant(minor)
        return det


def cofactors(M, Cof):
    n = len(M)
    m = len(M[0])
    zeroes(Cof, n)
    for i in range(n):
        for j in range(m):
            minor = []
            #minor = M.copy()
            copyMatrix(M, minor)
            getMinor(minor,i,j)
            Cof[i][j] = ((-1)**(i+j))*determinant(minor)

def transpose(M, T):
    n = len(M)
    m = len(M[0])
    zeroes(T, n)
    for i in range(n):
        for j in range(m):
            T[j][i] = M[i][j]

def inverseMatrix(M, Minv):
    det = determinant(M)
    # print("determinate de M")
    if det == 0:
        print("exit")
        exit()
    else:
        Cof = []
        Adj = []
        cofactors(M,Cof)
        transpose(Cof,Adj)
        productRealMatrix(1/det, Adj, Minv)

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