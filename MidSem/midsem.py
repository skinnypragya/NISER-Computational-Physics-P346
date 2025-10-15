# Name : Pragya Goyal
# Roll No : 2311127
# ------------------------------ Mid Semester Examination---------------------------------------

# Question 01 : Using the LCG pRNG constructed in class (a = 1103515245, c = 12345, m =
# 32768), determine the area of an ellipse, centered at origin, having semi-minor
# and semi-major axis of 1 and 2 unit respectively. Choose the number of random
# points such that the result is within 5% of the analytical value.
import matplotlib.pyplot as plt
from pragyalib import lcg

def areacalci(limit):
    # Generate 2*limit random numbers for x and y pairs
    rng = lcg()
    rand_nums = rng.lcg_gen(2 * limit, 0.7, 1103515245, 12345, 32768)
    # Scale to [0,1]
    rand_nums = [x / 32768 for x in rand_nums]
    # Split into x and y
    Lx = rand_nums[0:limit]
    Ly = rand_nums[limit:]
    # Scale to [-1,1] and [-2,2]
    Lx = [-1 + 2*x for x in Lx]
    Ly = [-2 + 4*y for y in Ly]

    count = 0
    for k in range(len(Lx)):
        if (Lx[k])**2 + (Ly[k])**2/4 <=1:   # Equation of ellipse when point is inside or above it
            count+=1
    area = count*8/limit
    return area

actual_area = 2 * 1 * 3.14159265359  # pi * a * b
tol = 0.05 * actual_area  # 5% tolerance
limit = 5
L_lim = []
L_area = []
while True:
    area = areacalci(limit)
    L_lim.append(limit)
    L_area.append(area)
    if abs(area - actual_area) <= tol:
        break
    limit += 1
print("limit for the 5% of acuracy is : ", limit)
    
# plt.plot(L_lim, L_area, label='Estimated Area')
# plt.axhline(actual_area, color='r', linestyle='--', label='Analytical Area')
# plt.xlabel('Number of Points')
# plt.ylabel('Estimated Area')
# plt.title(r"Plot when the difference in area is about $10^(-4)$")
# plt.legend()
# plt.show()
# limit for the 5% of acuracy is :  20

# Question 2 : Wein’s displacement law states that black body radiation for different tempera-
# tures peak at different wavelengths (λm) that are inversely proportional to the

# temperature T, i.e. λmT = b, where b is Wein’s constant. It can be derived from
# the Planck’s law for spectrum of black body radiation by solving

# (x − 5) e
# x + 5 = 0, where x =
# hc
# λmkT > 0

# Solve the above equation using Newton-Raphson method and determine Wein’s
# constant b in meter-Kelvin to a precision of 10−4

# . Take h = 6.626 × 10−34 m2 −

# kg/s, k = 1.381 × 10−23 m2 − kg/Ks2 and c = 3 × 108 m/s.

from pragyalib import roots
import math
def fun(x):
    return (x-5)*math.exp(x) + 5
def dfun(x):
    return (x-5)*math.exp(x) + math.exp(x)
root = roots().newton_raphson(fun, dfun, 10, 10**(-4))

# finding the value of Wein’s constant b
h = 6.626*(10**(-34))
c = 3*(10**8)
k = 1.381*(10**(-23))
print("root of the function is", root)
print("Value of Wein’s constant b is : ", (h*c)/(k*root))
# Output
'''root of the function (x-5)*math.exp(x) + 5 is 4.965114232019792
Value of Wein’s constant b is :  0.0028990103305774253
'''

# Question 3 Find the inverse of the following matrix (if exists) using LU decomposition
from pragyalib import LU_decomp, myLibrary
A = myLibrary().read_matrix("matA.txt")
print(LU_decomp().inverse(A))

# Question 4 Solve the linear system of equation A x = b, where A and b are given in the file
# msem gs.txt using Gauss-Seidel iterative methods to a precision of 10−6
# . [3]
