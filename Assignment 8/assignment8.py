# Name : Pragya Goyal, Roll No. : 2311127

# --------------------------- Assignement 8 ----------------------------------------

#------------------------------Question 1-------------------------------------------

# Find the solution for the following set of nonlinear equations using both fixed
# point and Newton-Raphson method. Compare their convergence rate.
from pragyalib import *
def fx1(x1,x2,x3): # function for x_1
    return (37 - x2)**0.5

def fx2(x1,x2,x3): # function for x_2
    return abs(x1-5)**0.5

def fx3(x1,x2,x3): # function for x_3
    return 3 - x1 - x2
x4 = 1
x5 = 1
x6 = 1

x0 = [x4,x5,x6]
g = [fx1,fx2,fx3]

L = roots().multivar_fixed(g,x0,10**(-6))
print("Roots of the equation using multivaribale fixed point method is : ", L[0])
print("number of iterations is : ", L[1])
# ------------------------------------------- OUTPUT --------------------------------------------------
# Roots of the equation using multivaribale fixed point method is :  [6.000000010757884, 1.0, -3.9999998709053854]
# number of iterations is :  11

def f1(x1,x2,x3):
    return x1**2 + x2 - 37
def f2(x1,x2,x3):
    return x1 - x2**2 - 5
def f3(x1,x2,x3):
    return x1 + x2 + x3 - 3

# Jacobian Construstion
def df1x1(x1,x2,x3):
    return 2*x1
def df1x2(x1,x2,x3):
    return 1
def df1x3(x1,x2,x3):
    return 0

def df2x1(x1,x2,x3):
    return 1
def df2x2(x1,x2,x3):
    return -2*x2
def df2x3(x1,x2,x3):
    return 0

def df3x1(x1,x2,x3):
    return 1
def df3x2(x1,x2,x3):
    return 1
def df3x3(x1,x2,x3):
    return 1

f = [f1,f2,f3]
# J = [[df1x1,df1x2,df1x3],[df2x1,df2x2,df2x3],[df3x1,df3x2,df3x3]]
def J_fun(x):
    return [[df1x1(x[0],x[1],x[2]),df1x2(x[0],x[1],x[2]),df1x3(x[0],x[1],x[2])],[df2x1(x[0],x[1],x[2]),df2x2(x[0],x[1],x[2]),df2x3(x[0],x[1],x[2])],[df3x1(x[0],x[1],x[2]),df3x2(x[0],x[1],x[2]),df3x3(x[0],x[1],x[2])]]
R = roots().multivar_newton(f,J_fun,x0,10**(-6))
print("Roots of the equation using multivariable newton_raphson is : ", R[0])
print("Number of iteration is : ", R[1])
# ------------------------------------------- OUTPUT --------------------------------------------------
# Roots of the equation using multivariable newton_raphson is :  [6.0, 1.0000000000000002, -4.0]
# Number of iteration is :  7








