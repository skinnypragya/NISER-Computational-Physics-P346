# Name : Pragya Goyal   Roll No : 2311127
# -------------------------------------------Question 1 ------------------------------------------
# Use Forward (explicit) Euler and Predictor-Corrector methods to solve and the
# following differential equations and compare with analytical form over range
# x ∈ [0, 2] and x ∈ [0, π/5] for the first and the second differential equations
# respectively. Use step size 0.1 in both the cases.

import math
import matplotlib.pyplot as plt
from pragyalib import solveDE
solve = solveDE()

def y1(x):
    return x**2 + 2*x + 2 -2*math.exp(x)

def y2(x):
    return math.tan(x + math.pi/4) - x

xo1 = []
for i in range(0, 2002):
    xo1.append(0 + i*0.001)
    if xo1[-1] >= 2:
        break
yo1 = [y1(i) for i in xo1]

xo2 = []
for i in range(0, 800):
    xo2.append(0 + i*0.001)
    if xo2[-1] >= math.pi/5:
        break
yo2 = [y2(i) for i in xo2]

def f1(x, y):
    return y - x**2

def f2(x, y):
    return (x + y)**2

x11, y11 = solve.euler(f1, [0, 2], 20, 0)
x12, y12 = solve.predcorrect(f1, [0, 2], 20, 0)

x21, y21 = solve.euler(f2, [0, math.pi/5], 7, 1)
x22, y22 = solve.predcorrect(f2, [0, math.pi/5], 7, 1)

plt.plot(xo1, yo1, label = r"Plot of actual function $x^2 + 2x + 2 - 2e^x$")
plt.plot(x11, y11, linestyle='dashed', label = "Plot from Euler method")
plt.plot(x12, y12, linestyle='dashed', label = "Plot from predictor-collector")
plt.xlabel("Values of x in [0, 2]")
plt.ylabel("Respective values of y")
plt.legend()
plt.show()

plt.plot(xo2, yo2, label = r"Plot of actual function")
plt.plot(x21, y21, linestyle='dashed', label = "Plot from Euler method")
plt.plot(x22, y22, linestyle='dashed', label = "Plot from predictor-collector")
plt.xlabel("Values of x in [0, pi/5]")
plt.ylabel("Respective values of y")
plt.legend()
plt.show()
