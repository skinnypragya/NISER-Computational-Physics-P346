def pol(F, x):
    # F: list of coefficients, highest degree first
    l = len(F)
    result = 0
    for i in range(l):
        result += F[i] * (x ** (l - 1 - i))
    return result

def defltn(P, r):
    # Synthetic division by (x - r)
    L = [P[0]]
    for i in range(1, len(P)):
        L.append(P[i] + r * L[i - 1])
    return L[:-1]  # Last element is remainder

def D(P):
    # Derivative of polynomial
    l = len(P)
    return [P[i] * (l - 1 - i) for i in range(l - 1)]

def laguerre(P, r, tol=1e-6, max_iter=100):
    roots = []
    P = P[:]
    while len(P) > 1:
        x = r
        for _ in range(max_iter):
            px = pol(P, x)
            if abs(px) < tol:
                break
            dp = pol(D(P), x)
            ddp = pol(D(D(P)), x)
            n = len(P) - 1
            G = dp / px
            H = G * G - ddp / px
            denom1 = G + ((n - 1) * (n * H - G * G)) ** 0.5
            denom2 = G - ((n - 1) * (n * H - G * G)) ** 0.5
            if abs(denom1) > abs(denom2):
                a = n / denom1
            else:
                a = n / denom2
            x = x - a
            if abs(a) < tol:
                break
        if abs(pol(P, x)) < tol:
            roots.append(x)
            P = defltn(P, x)
        else:
            break
    return [root for root in roots if abs(pol(P, root)) < tol]

# Example usage
print(laguerre([1, 0, -7, 6], 1, 1e-6))