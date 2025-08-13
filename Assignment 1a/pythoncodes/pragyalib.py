class myLibrary:
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
    def lcg_gen(self, limit, x, a, c, m):
        l = [x]
        for i in range(limit):
            l.append((a*l[-1] + c)%m)
        return l
