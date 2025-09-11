# Name : Pragya Goyal
# Roll No.: 2311127
# ---------------------------------- Assignement 9 ----------------------------------------------
# Question : 1
# Use Laguerre’s method and deflation to find the roots (all real) of the following
# three polynomials.
from pragyalib import poly_roots

print(poly_roots().laguerre_all([1,-1,-7,1,6], 10**(-6))) # example usage
print(poly_roots().laguerre_all([1,0,-5,0,4], 10**(-6)))
print(poly_roots().laguerre_all([2,0,-19.5,0.5,13.5,-4.5],10**(-6)))

# Output are the roots of the equations P1, P2, P3 respectively
#################################################################################################
# [1.0, -0.9999999999999651, 2.999999999999993, -2.0000000000000275]
# [1.0, 1.9999999997991764, -0.9999999991967057, -2.000000000602471]
# [0.5000634853669526, 0.499936512406658, -0.99999999706107, 2.9999999996473283, -3.0000000003598686]
##################################################################################################