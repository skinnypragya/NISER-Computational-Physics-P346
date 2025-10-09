# Name : Pragya Goyal           Roll No.: 2311127
# ----------------------------- Question 1 ----------------------------------------------
# Evaluate the following integrals using Midpoint and Simpson’s 1/3-rule accurate
# up to 6 places in decimal. Use the error bound formulae to determine N.
import math
import matplotlib.pyplot as plt
from pragyalib import integration
integ = integration()

def f1(x):
    return 1/x 
def f2(x):
    return x*math.cos(x)

# Using the upper bound formula for function 1 i.e. f1 we get the vaules of N as 
# N = 289 -------> For MidPoint method and
# N = 20  -------> For Simpsonsonethird method

print("The value of integration using midpoint method",integ.mid_integratn([1,2], f1, 289))
print("The value of integration using Simpsonsonethird method", integ.Simpsonsonethird([1,2], f1, 20))
''' ------------------------ Output 1-------------------
The value of integration using midpoint method 0.6931468064035272
The value of integration using Simpsonsonethird method 0.6931473746651163
'''
# Using the upper bound formula for function 2 i.e. f2 we get the vaules of N as 
# N = 610 -------> For MidPoint method and
# N = 22  -------> For Simpsonsonethird method

print("The value of integration using midpoint method",integ.mid_integratn([0, math.pi/2], f2, 610))
print("The value of integration using Simpsonsonethird method",integ.Simpsonsonethird([0, math.pi/2], f2, 22))
''' ------------------------ Output 2 ------------------
The value of integration using midpoint method 0.5707970370864707
The value of integration using Simpsonsonethird method 0.570796987316687
'''
#--------------------------------------- Question 2 -------------------------------------
# Use Monte Carlo integration scheme (using your own pRNG) to estimate the
# integral accurate up to 4 places in decimal
def g(x):
    return (math.sin(x))**2

L_x = []
L_y = []

for i in range(20,9000):
    L_x.append(i)
    L_y.append(integ.monte_carlo(10000, [-1,1], g, i))
    if abs(L_y[0] - 0.545351286) <= 10**(-6): # Comparing it with actual value
        break

plt.plot(L_x, L_y)
plt.xlabel(r"Values of $\mathbf{N}$")
plt.ylabel(r"Values of $\mathbf{integration}$")
plt.title("Plot for the converges upto three decimal places")
plt.show()
#print(integ.monte_carlo(10000, [-1,1], g, 4000))

# Plot is attached in the file!