import matplotlib.pyplot as plt
import time
import random

def naive_multiplication(A, B):
    n = len(A)
    m = len(B)
    result = [0] * (n + m - 1)

    for i in range(n):
        for j in range(m):
            result[i + j] += A[i] * B[j]
    return result

def fft_multiplication(A, B):
    """
    Multiplies two polynomials A and B using Fast Fourier Transform (FFT)
    A and B are lists of coefficients, where the i-th element represents the coefficient x^i.
    """
    from FFT import fastFouriertransform
    fft = fastFouriertransform()

    # Determine size = next power of 2 >= len(A)+len(B)-1
    n = 1
    while n < len(A) + len(B) - 1:
        n *= 2

    A_pad = A[:] + [0] * (n - len(A))
    B_pad = B[:] + [0] * (n - len(B))

    FA = fft.FFT(A_pad)
    FB = fft.FFT(B_pad)

    FC = [FA[i] * FB[i] for i in range(n)]

    C = fft.IFFT(FC)

    C = [round(c.real / n) for c in C]
    return C[:len(A) + len(B) - 1]

# Performance Test
degrees = [2**d for d in range(10, 15)]  # 8, 16, ..., 1024
fft_times = []
naive_times = []

for d in degrees:
    A = [random.randint(-10, 10) for _ in range(d)]
    B = [random.randint(-10, 10) for _ in range(d)]

    # FFT timing
    start = time.perf_counter()
    fft_multiplication(A, B)
    fft_times.append(time.perf_counter() - start)

    # Naive timing
    start = time.perf_counter()
    naive_multiplication(A, B)
    naive_times.append(time.perf_counter() - start)

# Plot Results
plt.figure(figsize=(10, 6))
plt.plot(degrees, fft_times, marker='o', label="FFT Multiplication")
plt.plot(degrees, naive_times, marker='o', label="Naive Multiplication")

plt.xscale("log", base=2)
plt.yscale("log")
plt.xlabel("Polynomial Degree (log scale)")
plt.ylabel("Time (seconds, log scale)")
plt.title("Polynomial Multiplication: FFT vs Naive")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.legend()
plt.tight_layout()
plt.show()
