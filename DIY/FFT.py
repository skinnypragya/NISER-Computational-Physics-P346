import cmath
class fastFouriertransform:
    def __init__(self):
        pass
    
    def multiply(self, A, B):
        n = len(A)
        m = len(B)
        result = [0] * (n + m - 1)

        for i in range(n):
            for j in range(m):
                result[i + j] += A[i] * B[j]
        return result

    def FFT(self, P):
        '''
            P = [a0, a1, ..., an-1] represents the polynomial
        '''
        n = len(P)
        if n == 1: return P

        omega = cmath.exp(2j * cmath.pi / n)
        Peven = P[0::2] # even degree coefficients
        Podd = P[1::2] # odd degree coefficients

        yeven = self.FFT(Peven)
        yodd = self.FFT(Podd)

        y = [0] * n
        for k in range(n // 2):
            y[k] = yeven[k] + omega**k * yodd[k]
            y[k + n // 2] = yeven[k] - omega**k * yodd[k]
        
        return y

    def IFFT(self, P):
        '''
            P = [p0, P1, ..., Pn-1] represents the values of the polynomial at n-th roots of unity
        '''
        n = len(P)
        if n == 1: return P

        omega = cmath.exp(-2j * cmath.pi / n) # just changed one line of code
        Peven = P[0::2] # even degree coefficients
        Podd = P[1::2] # odd degree coefficients

        yeven = self.IFFT(Peven)
        yodd = self.IFFT(Podd)

        y = [0] * n
        for k in range(n // 2):
            y[k] = yeven[k] + omega**k * yodd[k]
            y[k + n // 2] = yeven[k] - omega**k * yodd[k]
        
        return y
