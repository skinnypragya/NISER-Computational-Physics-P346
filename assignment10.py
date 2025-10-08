# Name : Pragya Goyal      Roll. No. : 2311127
#---------------------------------- Question 1 ------------------------------------------------
# Using both Midpoint and Trapezoidal method evaluate the following integrals
# and compare with the analytical results, for N = 4, 8, 15, 20. Present the result
# in tabular form.
import math
from pragyalib import integration

def f1(x):
    return 1/x
def f2(x):
    return x*(math.cos(x))
def f3(x):
    return x*(math.atan(x))

# print(integration().mid_integratn([1,2], f1, 20))
# print(integration().mid_integratn([0,math.pi/2], f2, 20))
# print(integration().mid_integratn([0,1], f3, 20))

# print(integration().trap_integratn([1,2], f1, 20))
# print(integration().trap_integratn([0,math.pi/2], f2, 20))
# print(integration().trap_integratn([0,1], f3, 20))

L = [4, 8, 15, 20]
print("For midPoint method")
for i in L:
    print(i,integration().mid_integratn([1,2], f1, i))
    print(i,integration().mid_integratn([0,math.pi/2], f2, i))
    print(i,integration().mid_integratn([0,1], f3, i))
print("For trapezium method")
for i in L:
    print(i,integration().trap_integratn([1,2], f1, i))
    print(i,integration().trap_integratn([0,math.pi/2], f2, i))
    print(i,integration().trap_integratn([0,1], f3, i))

'''
Results :
    Using MidPoint Method
        for integration function f1: 
            N = 4  -->  0.6912198912198912
            N = 8  -->  0.6926605540432034
            N = 15 -->  0.6930084263712958
            N = 20 -->  0.6930690982255869
        for integration function f2:
            N = 4  -->  0.5874479167573121
            N = 8  -->  0.5749342733821311
            N = 15 -->  0.5719716590967575
            N = 20 -->  0.5714572867152204
        for integration function f3:
            N = 4  -->  0.2820460493571144
            N = 8  -->  0.2845610193056679
            N = 15 -->  0.28516010270349235
            N = 20 -->  0.28526426016144524
    Using Trapezium Method
        for integration function f1:
            N = 4  -->  0.6970238095238095
            N = 8  -->  0.6941218503718504
            N = 15 -->  0.6934248043580644
            N = 20 -->  0.6933033817926942
        for integration function f2:
            N = 4  -->  0.5376071275673586
            N = 8  -->  0.5625275221623353
            N = 15 -->  0.5684462350385162
            N = 20 -->  0.569474588169518
        for integration function f3:
            N = 4  -->  0.2920983458939516
            N = 8  -->  0.28707219762553304
            N = 15 -->  0.285874264217412
            N = 20 -->  0.285665963360493
'''