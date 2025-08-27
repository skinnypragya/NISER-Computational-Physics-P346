# Name : Pragya Goyal              Roll No. : 2311127
# ---------------------------------Assignment 4 -----------------------------------------------#
# Question : 01 
# Use Cholesky factorization for the matrix A and solve for Ax = b for the following.
from pragyalib import *
A = myLibrary().read_matrix("matrixA.txt")
B = myLibrary().read_matrix("matrixB.txt")

print("The Cholesky Tranformed matrix is : ", hermi_cholesky().cholesky(A))
print("Matrix solution of the Linear Equation is : ", hermi_cholesky().cholesky_solve(myLibrary().read_matrix("matrixA.txt"),B))

##########################################################
# Matrix solution of the Linear Equation is :  [[0.0], [1.0], [1.0], [1.0000000000000002]]
##########################################################

# Question : 02
# Use Jacobi iterative method to solve the above matrix to a precision of 10−6

# Jacobi Iterative Method
A = myLibrary().read_matrix("matrixA.txt")
B = myLibrary().read_matrix("matrixB.txt")

result = Jacobi().jacobi_iter(A,B)
print("The Jacobi Iterative Method solution is : ", result)

########################################################################
# The Jacobi Iterative Method solution is :  [[0.0], [0.9999994039535522], [0.9999997019767761], [0.9999997019767761]]
########################################################################