def Multiply(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        xx = []
        for j in range(len(matrix2[0])):
            tmp = 0
            for k in range(len(matrix2)):
                tmp += matrix1[i][k]*matrix2[k][j]
            xx.append(tmp)
        result.append(xx)
    return result

def Transpose(matrix):
    result = []
    for j in range(len(matrix[0])):
        xx = []
        for i in range(len(matrix)):
            xx.append(matrix[i][j])
        result.append(xx)
    return result

def SubMatrix(matrix, a, b):
    result = []
    for i in range(len(matrix)):
        xx = []
        for j in range(len(matrix[0])):
            if i != a and j != b:
                xx.append(matrix[i][j])
        if len(xx) != 0:
            result.append(xx)
    return result

def Determinant(matrix):
    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    else:
        result = 0
        for i in range(len(matrix)):
            result += (-1)**i * matrix[0][i]*Determinant(SubMatrix(matrix, 0, i))
        return result

def Inverse(matrix):
    det = Determinant(matrix)
    if len(matrix) == 2:
        return [[float(matrix[1][1])/det, -float(matrix[0][1])/det], [-float(matrix[1][0])/det, float(matrix[0][0])/det]]
    else:
        cofactors = []
        for i in range(len(matrix)):
            row = []
            for j in range(len(matrix)):
                submatrix = SubMatrix(matrix, i, j)
                row.append((-1)**(i+j) * Determinant(submatrix))
            cofactors.append(row)
        cofactors = Transpose(cofactors)
        for i in range(len(cofactors)):
            for j in range(len(cofactors)):
                cofactors[i][j] = float(cofactors[i][j])/det
        return cofactors

def Matrix(n, m):
    result = []
    for i in range(1, n+1):
        xx = []
        for j in range(m+1):
            xx.append(i**j)
        result.append(xx)
    return result

def Coefficient_A(start, end, m, Y):
    n = end - start + 1
    matrix = Matrix(n, m)
    matrix_T = Transpose(matrix)
    mul1 = Multiply(matrix_T, matrix)
    inv1 = Inverse(mul1)
    mul2 = Multiply(inv1, matrix_T)
    A = Multiply(mul2, Transpose([y[start:end+1]]))
    return A

def pi(i, m, A):
    result = 0
    for idx in range(m+1):
        result += A[idx][0]*(i**idx)
    return result

def LeastSquareError(Y, m, start, end):
    if start == end:
        return 0
    elif end - start == 1:
        return 0
    else:
        A = Coefficient_A(start, end, m, Y)
        error = 0
        for i in range(start, end+1):
            error += (pi(i-start+1, m, A) - Y[i])**2
        return error

def MinLeastSquareError(start, end, m, C, y, partition):
    result = []
    for i in range(n):
        result.append(0)
    for i in range(n):
        if i == 0 or i == 1:
            continue
        error = partition[(0, i)]
        for j in range(1, i+1):
            tmp = result[j-1] + partition[(j, i)] + C
            error = min(error, tmp)
        result[i] = error
    return result[end]

if __name__ == '__main__':
    n, m, C = [ int(num) for num in input().split()] # get the parameters
    y = [int(num) for num in input().split()] # get y

    partition = {} # Use a dictionary to store the error
    for i in range(n):
        for j in range(n-i):
            partition[(i,j+i)] = LeastSquareError(y, m, i, j+i)
    print(int(MinLeastSquareError(0, n-1, m, C, y, partition)))

# No Collaborators
