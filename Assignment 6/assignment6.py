# Name : Pragya Goyal  Roll No.: 2311127

# Question 1 : Find the root of the following function in the interval [1.5, 3.0] to an accuracy of
# 10−6 using both Bisection and Regula Falsi method.
# f(x) = log(x/2) − sin(5x/2)

import math
from pragyalib import *

def function1(x):
    return math.log(x/2) + math.sin(5*x/2)

def function2(x):
    return -x-math.cos(x)

a,b = roots().bracketing(function1,1.5,3)
result1 = roots().bisecting(function1,a,b,10**-6)
result2 = roots().regula_falsi(function1,a,b,10**-6)

print("The root of the function f(x) = log(x/2) - sin(5x/2) using bisection in the interval is [1.5,3] is : \n",result1)
print(f"Value of function at {result1} is {function1(result1)}")

print("The root of the function f(x) = log(x/2) - sin(5x/2) using regula falsi in the interval is [1.5,3] is : \n",result2)
print(f"Value of function at {result2} is {function1(result2)}")
# -------------------------------------- OUTPUT ------------------------------------------------------
# The root of the function f(x) = log(x/2) - sin(5x/2) using bisection in the interval is [1.5,3] is : 
#  2.4341747760772705
# Value of function at 2.4341747760772705 is -1.4612460373097935e-06
# The root of the function f(x) = log(x/2) - sin(5x/2) using regula falsi in the interval is [1.5,3] is :
#  2.4341752866283444
# Value of function at 2.4341752866283444 is -1.7957857423311907e-14
# -------------------------------------------------------------------------------------------------------------------------------------------------

# Question 2 : 
# Consider the following non-linear equation
# f(x) = −x − cos(x)
# Find an appropriate interval bracket in which the root possible is, starting with
# the interval [2, 4].

a1,b1 = roots().bracketing(function2,2,4)
result3 = roots().bisecting(function2,a1,b1,10**-6)
print("The bracketing interval for the function f(x) = -x - cos(x) is : ",[a1,b1])
# print(f"The root of the equation in interval {[a1,b1]} is {result3}")
# print(f"The value of function at {result3} is : ", function2(result3))
# -----------------------------------------OUTPUT-----------------------------------------
# The bracketing interval for the function f(x) = -x - cos(x) is :  [-1.1874849202000002, 4]