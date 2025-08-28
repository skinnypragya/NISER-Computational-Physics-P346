#-------------------------Assignment 5-----------------------------#
# Name = Pragya Goyal -------- Roll No.: 2311127-------------------#

# Question : 01 Solve the following linear equation by Cholesky decomposition (check for sym-
# metric matrix) and Gauss-Seidel to a precision of 10−6

from pragyalib import *

A = myLibrary().read_matrix("matrixA.txt")
B = myLibrary().read_matrix("matrixB.txt")
n = len(A)
if all((A[i][j] == A[j][i] for j in range(n)) for i in range(n)):
    result = hermi_cholesky().cholesky_solve(A,B) # solving from cholesky method
    print(f"Solution of the equation using Cholesky is {result}")

# Gauss Seidel Method
A = myLibrary().read_matrix("matrixA.txt")
B = myLibrary().read_matrix("matrixB.txt")

result2, iter2 = gauss_seidel().gauss_iter(A,B,[[0] for _ in range(len(A))])
print(f"Solution of equations using Gauss Seidel is {result2} \n with iterations of {iter2}")
#####################################################################################
# Solution of the equation using Cholesky is [[1.0], [0.9999999999999999], [1.0], [1.0], [1.0], [1.0]]
# Solution of equations using Gauss Seidel is [[0.9999997530614102], [0.9999997892247294], [0.9999999100460266], [0.9999998509593769], [0.9999998727858708], [0.9999999457079743]]
#  with iterations of 16
#####################################################################################


# Question : 2 Solve the following linear equation by
# Jacobi & Gauss-Seidel (with rearranging to make diagonally dominant using
# code) to a precision of 10−6

C = myLibrary().read_matrix("matrixC.txt")
D = myLibrary().read_matrix("matrixD.txt")
C = [[11, 3, 0, 1, 2], [0, 4, 2, 0, 1], [3, 2, 7, 1, 0],[4, 0, 4, 10, 1],[2, 5, 1, 3, 13]]
D = [[51],[15], [15], [20], [92]]
# making diagonally dominant
# def make_diagonally_dominant(A, B):
#     n = len(A)
#     for i in range(n):
#         max_row = i
#         for j in range(i, n):
#             diag = abs(A[j][i])

#             # calculate row sum without using sum()
#             off_diag_sum = 0
#             for k in range(n):
#                 if k != i:
#                     off_diag_sum += abs(A[j][k])

#             if diag >= off_diag_sum and diag > abs(A[max_row][i]):
#                 max_row = j

#         # swap rows if needed
#         if max_row != i:
#             A[i], A[max_row] = A[max_row], A[i]
#             B[i], B[max_row] = B[max_row], B[i]
#     return A, B

result3 = jacobi().jacobi_iter(C,D,[[0] for _ in range(len(C))]) # Jacobi solution
result4 = gauss_seidel().gauss_iter(C,D,[[0] for _ in range(len(C))]) # Gauss_seidel solution
result5 = gauss_jordan().jordan(C,D) # checking using gauss jordan
print("Solution form jacobi iterations is : \n", result3)
print("Solutions from gauss_seidel iterations is : \n", result4)
print("Checking and comparing using gauss jordan elimination : \n",result5)

######################################################################################
# Solution form jacobi iterations is : 
#  ([[2.9791649583226008], [2.215599258220273], [0.21128373337161171], [0.15231661140963978], [5.71503326456748]], 58)
# Solutions from gauss_seidel iterations is : 
#  ([[2.979165086347139], [2.215599676186742], [0.21128402698819157], [0.15231700827754802], [5.715033568811629]], 12)
# Checking and comparing using gauss jordan elimination : 
#  [[2.9791651927838703], [2.215599575521755], [0.2112840466926067], [0.15231694375663274], [5.7150336045277665]]
######################################################################################