class myLibrary:
    def __init__(self):
        pass
    def read_matrix(self, filename) :
        with open(filename, 'r' ) as f :
            matrix = []
            for line in f :
                row = [float (num) for num in line.strip( ).split( )]
                matrix.append(row)
        return matrix

    def matrix_multi(self, a, b):
        nrowa= len(a)
        ncolumna = len(a[0])
        nrowb = len(b)
        ncolumnb = len(b[0])
        answer = []
        for i in range(nrowa):
            row = []
            for j in range(ncolumnb):
                val = 0
                for k in range(ncolumna):
                    val += a[i][k] * b[k][j]
                row.append(val)
            answer.append(row)
        return answer

    def transpose(self, mat):
        nrow = len(mat)
        ncolumn = len(mat[0])
        answer = []
        for i in range(ncolumn):
            row = []
            for j in range(nrow):
                row.append(mat[j][i])
            answer.append(row)
        return answer
    
    

class myComplex:
    def __init__(self, a, b):
        self.real = a
        self.img = b
    def show(self):
        return f"{self.real} + {self.img}j"
    
    def sum(self, s, a, b):
        if s == "+" :
            return f"{self.real + a : .4f} + {self.img + b : .4f}j"
        elif s == "-" :
            return f"{self.real - a : .4f} + {self.img - b : .4f}j"
        elif s == "*" :
            return f"{self.real * a - self.img * b : .4f} + {self.real * b + self.img * a : .4f}j"
        else:
            return "enter valid operation!"
    def modC(self):
        return f"{((self.real)**2 + (self.img)**2)**0.5 : .4f}"

class lcg:
    def __init__(self):
        pass
    def lcg_gen(self, limit, x, a, c, m):
        l = [x]
        for i in range(limit):
            l.append((a*l[-1] + c)%m)
        return l
class gauss_jordan:
    def __init__(self):
        pass
    def jordan(self, A, B):
        T = [A[i][:] + B[i] for i in range(len(A))]
        z = len(T)
        for i in range(z):
            dig = T[i][i] # value of diagonal elements

            if dig == 0:
                for r in range(i + 1, z): # check for non-zero pivot
                    if T[r][i] != 0:
                        T[i], T[r] = T[r], T[i] # swap
                        break
                dig = T[i][i]
                if dig == 0: # again if diagonal is zero then lines are parallel and no solution
                    return "No Solution"

            for j in range(i, len(T[0])):
                T[i][j] /= dig
            for k in range(z):
                if k != i:
                    f = T[k][i] # factor to eliminate
                    for l in range(i, len(T[0])):
                        T[k][l] -= f * T[i][l]
        # return A               
        C = []
        for w in range (z):
            C.append(T[w][-len(B[0]):])
        return C
    
    def det(self, A):
        c = 0
        for i in range(len(A)):
            dig = A[i][i]
            if dig == 0:
                for r in range(i + 1, len(A)): # check for non-zero pivot
                    if A[r][i] != 0:
                        A[i], A[r] = A[r], A[i] # swap
                        c +=1
                        break
                dig = A[i][i]
                if dig == 0: # again if diagonal is zero then determinant is zero
                    return "det is zero"
            for k in range(len(A)):
                if k > i:
                    f = A[k][i]/dig
                    for l in range(i, len(A)):
                        A[k][l]-= f*A[i][l]
        return A

    def identity(self, mat):
        l = len(mat)
        return [[1 if i == j else 0 for j in range(l)] for i in range(l)]
class LU_decomp:
    def __init__(self):
        pass
    def storeLU(self,A): # Gives the elements of L and U in single Matrix
        val = len(A)
        # ============== Using DOOLITTLE Composition ==================== #
        for i in range(val):
            A[0][i] = A[0][i]
        for j in range(1,val):
            A[j][0] = A[j][0] / A[0][0]
        for i in range(1,val):
            for j in range(1,val):
                if j<=i:
                    sum = 0
                    for k in range(0, j):
                        sum+= A[j][k]*A[k][i]
                    A[j][i] -= sum
                else:
                    sum = 0
                    for k in range(0, i):
                        sum += A[j][k]*A[k][i]
                    A[j][i] = (A[j][i] - sum) / A[i][i]
        return A
