from pragyalib import *
import math
# Name : Pragya Goyal    Roll No. : 2311127
# ----------------------------------- Question 1 -----------------------------------------#
# Find the root of the following function in the interval [−1.5, 1.5] to an accuracy
# of 10−6 using Bisection, Regula Falsi and Newton-Raphson methods. Compare
# their convergence rate.

def function1(x):
    return 3*x + math.sin(x) - math.exp(x)
def function2(x):
    return 3 + math.cos(x) - math.exp(x)
def g(x):
    return (math.exp(x) - math.sin(x)) / 3

a,b = roots().bracketing(function1,-1.5,1.5)

print("Root of the equation 3x + sin(x) - e^(x) in the interval [-1.5,1.5] is using Bisection : ",roots().bisecting(function1,a,b,10**-6))
print("Root of the equation 3x + sin(x) - e^(x) in the interval [-1.5,1.5] is using regula_falsi: ",roots().regula_falsi(function1,a,b,10**-6))
# print("Root of the equation 3x + sin(x) - e^(x) in the interval [-1.5,1.5] is using Fixed point method : ",roots().fixed_point(g,1,10**-6))
print("Root of the equation 3x + sin(x) - e^(x) in the interval [-1.5,1.5] is using Newton raphson method : ",roots().newton_raphson(function1, function2,1,10**-6))

################################################################################################################################################################################################
# Root of the equation 3x + sin(x) - e^(x) in the interval [-1.5,1.5] using Bisection method :  0.36042237281799316
# Root of the equation 3x + sin(x) - e^(x) in the interval [-1.5,1.5] using regula_falsi method :  0.3604217029603244
# Root of the equation 3x + sin(x) - e^(x) in the interval [-1.5,1.5] using Newton raphson method :  0.36042170296019965 
################################################################################################################################################################################################

#--------------------------------------------- Question 2 --------------------------------------------------------------
# Find the root of the following function using fixed point method
def function3(x):
    return x**2 - 2*x - 3
def g2(x):
    return 2 + 3/x
def g3(x):
    return 3/(x-2)
print("1st Root of the function x^2 - 2x -3 around 2.5 is : ", roots().fixed_point(g2,2.5,10**-6) )
print("2nd Root of the function x^2 - 2x -3 around 2.5 is : ", roots().fixed_point(g3,0,10**-6) )

#####################################################################################################################
# 1st Root of the function x^2 - 2x -3 around 2.5 is :  2.9999998805284847
# 2nd Root of the function x^2 - 2x -3 around 2.5 is :  -1.0000000929222947
#####################################################################################################################
