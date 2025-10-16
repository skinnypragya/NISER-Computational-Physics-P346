# Name : Pragya Goyal        Roll No: 2311127
# Question 1 Use appropriate n-point Gaussian quadrature to evaluate
# accurate up to 9 places in decimal.accurate up to 9 places in decimal.
from pragyalib import integration
def f1(x):
    return x**2/(1+x**4)

n = 6
while True:
    I = integration().gaussquad_legend(f1,[-1,1], n)
    if abs(I - 0.4874954940) <= 10**(-9): # for nine place accuracy
        print("Order :",n) 
        print("Value of integration :", I)
        break
    n+=1
'''
----------------------------------------Output------------------------------------------------
Order : 14
Value of integration : 0.48749549425855665
'''
# Question : 2 
# Use Simpson’s rule and appropriate Gaussian quadrature to evaluate the following
# integral accurate up to 8 or 9 places in decimal

def f2(x):
    return (1+x**4)**0.5
n = 18
while True:
    I = integration().Simpsonsonethird([0, 1], f2, n)
    if abs(I - 1.0894294130) <= 10**(-10): # correct upto nine decimal places
        print("Order : ", n)
        print("Value of integration : ", I)
        break
    n+=1
n = 4
while True:
    I = integration().gaussquad_legend(f2,[0,1], n)
    if abs(I - 1.0894294130) <= 10**(-9): # for nine place accuracy
        print("Order :",n) 
        print("Value of integration :", I)
        break
    n+=1
'''
---------------------------------------- Output ---------------------------------------------
    Order :  21
    Value of integration :  1.0894294129750703 # From Simpson's
    Order : 8
    Value of integration : 1.0894294131091897 # From Gauss Quad
'''