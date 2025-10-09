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
                T[i][j] /=  dig
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
    def forback(self,A,B):
        val = len(A)
        result = self.storeLU(A)

        # Forward substitution: solve L * Y = B
        Y = [[0] for _ in range(val)]
        Y[0][0] = B[0][0] 

        for i in range(1, val):
            sum1 = 0
            for j in range(i):
                sum1 += result[i][j] * Y[j][0]
            Y[i][0] = B[i][0] - sum1            

        # Back substitution: solve U * X = Y
        X = [[0] for _ in range(val)]
        X[-1][0] = Y[-1][0] / result[-1][-1]

        for i in range(val-2, -1, -1):
            sum2 = 0
            for j in range(i+1, val):
                sum2 += result[i][j] * X[j][0]
            X[i][0] = (Y[i][0] - sum2) / result[i][i]
        
        return X
    
    def det(self, A):
        D = self.storeLU(A)
        p = 1
        for i in range(len(D)):
            p *= D[i][i]
        return p
class hermi_cholesky:
    def __init__(self):
        pass
    def cholesky(self, A):
        n = len(A)
        for i in range(n):
            sum1 = 0
            for j in range(i):
                sum1 += A[i][j]**2
            A[i][i] = (A[i][i] - sum1)**0.5
            for j in range(n):
                if i < j :
                    sum2 = 0
                    for k in range(i):
                        sum2 += A[i][k]*A[k][j]
                    A[i][j] = (A[i][j] - sum2) / A[i][i]
                    A[j][i] = A[i][j]
        return A
    def cholesky_solve(self, A, B):
        n = len(A)
        L = self.cholesky(A)
        
        # Forward substitution to solve L * Y = B
        Y = [[0] for _ in range(n)]
        for i in range(n):
            sum1 = 0
            for j in range(i):
                sum1 += L[i][j] * Y[j][0]
            Y[i][0] = (B[i][0] - sum1) / L[i][i]
        
        # Back substitution to solve L^T * X = Y
        X = [[0] for _ in range(n)]
        for i in range(n-1, -1, -1):
            sum2 = 0
            for j in range(i+1, n):
                sum2 += L[j][i] * X[j][0]
            X[i][0] = (Y[i][0] - sum2) / L[i][i]
        
        return X
class jacobi:
    def __init__(self):
        pass
    
    def jacobi_iter(self,A,B,seed):
        n = len(A)
        D = [[A[i][j] if i==j else 0 for j in range(n)] for i in range(n)]
        T = [[A[i][j] if i != j else 0 for j in range(n)] for i in range(n)]

        for t in range(1,100): # iterative steps
            new_seed = [[0] for _ in range(n)]
            for i in range(n):
                sum1 = 0
                for j in range(n):
                    if i != j:
                        sum1 += T[i][j] * seed[j][0]
                new_seed[i][0] = (B[i][0] - sum1) / D[i][i]

            if all(abs(new_seed[i][0] - seed[i][0]) < 10**(-6) for i in range(n)):
                # check if the difference is difference is very less for more precision!
                return new_seed, t
            seed = new_seed # change the seed

class gauss_seidel:
    def __init__(self):
        pass
    
    def gauss_iter(self, A, B, x):
        n = len(A)
        
        
        for k in range(100):
            x_new = [[0] for _ in range(n)]
            
            for i in range(n):
                sum1 = 0
                sum2 = 0
                for j in range(n):
                    if j < i:
                        sum1 += A[i][j] * x_new[j][0]
                    if j > i:
                        sum2 += A[i][j] * x[j][0]

                x_new[i][0] = (B[i][0] - sum1 - sum2) / A[i][i]
            
            if all(abs(x_new[i][0] - x[i][0]) < 10**(-6) for i in range(n)):
                return x_new, k + 1
            
            x = x_new

class roots:
    def __init__(self):
        pass
    def bracketing(self,f, a, b):
        beta = 0.1
        while f(a) * f(b) >= 0: # ensure that the root is bracketed
            if abs(f(a)) < abs(f(b)):
                a-= beta*(b-a)
            else:
                b+= beta*(b-a)
        return a,b # return the bracketing interval
    def bisecting(self,f,a,b,tol):
        while abs((b - a) / 2) > tol: # while the interval is larger than tolerance
            mid = (a + b) / 2
            if f(mid) == 0:
                return mid
            elif f(a) * f(mid) < 0:
                b = mid
            else:
                a = mid
        return (a + b) / 2 # return midpoint
    
    def regula_falsi(self,f, a, b, tol):
        while abs(b - a) > tol:
            c = (a * f(b) - b * f(a)) / (f(b) - f(a))  # Regula Falsi formula
            if f(c) == 0:
                return c  # Found exact root
            elif f(a) * f(c) < 0:
                b = c  # Root is in left subinterval
            else:
                a = c  # Root is in right subinterval
        

        return (a + b) / 2  # Return midpoint as the root approximation
    
    def fixed_point(self, g, x0, tol):
        max_iter = 100
        for i in range(max_iter):
            x1 = g(x0)
            if abs(x1 - x0) < tol:
                return x1 # write "return x1, i" if you want the number of iterations
            x0 = x1
        return x0  # Return the last approximation if not converged

    def newton_raphson(self, f, df, x0, tol):
        max_iter = 100
        for i in range(max_iter):
            fx0 = f(x0)
            dfx0 = df(x0)

            x1 = x0 - fx0 / dfx0 # Iterative formula
            if abs(x1 - x0) < tol:
                return x1 # write "return x1, i" if you want the number of iterations
            x0 = x1
        return x0  # Return the last approximation if not converged
    
    def multivar_fixed(self, g, x0, tol):
        # g and x0 are lists of functions and initial guess
        max_iter = 100
        n = len(x0)
        for i in range(max_iter):
            x1 = [0] * n
            for j in range(n):
                x1[j] = g[j](*x0)  # Evaluate g_j at the current guess x0

            if all(abs(x1[j] - x0[j]) < tol for j in range(n)):
                return x1, i
            x0 = x1
        return x0  # Return the last approximation if not converged
    
    # multivariable newton raphson for n variables
    def multivar_newton(self, f, J, x0, tol):
        # f is a list of functions, J is a function that returns the Jacobian matrix
        max_iter = 100
        n = len(x0)
        for i in range(max_iter):
            F = [f[j](*x0) for j in range(n)]  # Evaluate f at the current guess x0
            J_matrix = J(x0)  # Get the Jacobian matrix at x0

            # Solve J * delta = -F using Gaussian elimination or any other method
            delta = gauss_jordan().jordan(J_matrix, [[-F[j]] for j in range(n)])

            x1 = [x0[j] + delta[j][0] for j in range(n)]  # Update the guess

            if all(abs(x1[j] - x0[j]) < tol for j in range(n)):
                return x1, i  
            x0 = x1
        return x0  # Return the last approximation if not converged

class poly_roots:
    def __init__(self):
        pass
    def pol(self,F,x): # F is list of coefficients of polynomial
        l = len(F)
        sum = 0
        for i in range(l):
            sum += F[i]*(x**(l-i-1))
        return sum
     
    def defltn(self,P,r): # divide P by divisor r
        L = []
        L.append(P[0])
        for i in range(1,len(P)):
            L.append(P[i] + r*L[i-1])
        
        return L[:-1]

    def D(self,P): # derivative of a polynomial function
        l = len(P)
        L = []
        for i in range(l-1):
            L.append(P[i]*(l-1-i))
        return L

    def laguerre(self,P, r, tol, iter=100):
        n = len(P) - 1
        for _ in range(iter):
            if abs(self.pol(P, r)) < tol:
                return r
            
            G = self.pol(self.D(P), r) / self.pol(P, r)
            H = G * G - self.pol(self.D(self.D(P)), r) / self.pol(P, r)
            denom1 = G + ((n - 1) * (n * H - G * G))**0.5
            denom2 = G - ((n - 1) * (n * H - G * G))**0.5
            if abs(denom1) > abs(denom2):
                a = n / denom1
            else:
                a = n / denom2
            r -= a
        return r 

    def laguerre_all(self,P, tol):
        roots = []
        poly = P[:]
        while len(poly) > 2:
            root = self.laguerre(poly, 1.0, tol)  # start guess = 1.0
            roots.append(root)
            poly = self.defltn(poly, root)
        if len(poly) == 2:
            roots.append(-poly[1] / poly[0])
        return roots

class integration:
    def __init__(self):
        pass

    def mid_integratn(self, Interval, function, parts):
        sum = 0
        h = (Interval[1] - Interval[0])/parts
        for i in range(1,parts+1):
            x = ((Interval[0] + (i-1)*h) + (Interval[0] + i*h))/2 # mid point of each interval 
            sum += h*function(x)
        return sum
    
    def trap_integratn(self, Interval, function, parts):
        sum = 0
        h = (Interval[1] - Interval[0])/parts
        for i in range(1,parts+1):
            x = Interval[0] + (i-1)*h
            y = Interval[0] + i*h
            sum += h*(function(x)+function(y))/2
        return sum

    def Simpsonsonethird(self, Interval, function, parts):
        if parts % 2 == 1: # if parts is odd then make it even
            parts += 1
        h = (Interval[1] - Interval[0])/parts
        sum = function(Interval[0]) + function(Interval[1])
        for i in range(1, parts, 2):
            x = Interval[0] + i*h
            sum += 4*function(x) # Adding based on formula
        for i in range(2, parts-1, 2):
            x = Interval[0] + i*h
            sum += 2*function(x) # Adding based on formula
        sum *= h/3
        return sum
    
    def monte_carlo(self, iter, Interval, function, parts):
        L = lcg().lcg_gen(iter, 10, 1103515245, 12345, 32768)
        for i in range(len(L)):
            L[i] /= 32768 # Getting all random numebr less than 1
        sum = 0
        for i in range(parts):
            x = Interval[0] + (Interval[1] - Interval[0]) * L[i] # Scaling numbers in range
            sum += function(x)
        return sum*(Interval[1] - Interval[0])/parts
