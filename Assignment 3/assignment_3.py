# Name : Pragya Goyal   Roll No.:2311127

# Assignment 3 Question : 1
# Find LU decomposition of the matrix and verify. The LU decomposition routine
# must be kept in the library for later use. Mention your choice of Doolittle or
# Crout clearly.

from pragyalib import *
A = myLibrary().read_matrix("matrixA.txt")
print("original matrix : ", A)
answer = LU_decomp().storeLU(A)
L = [[0 for j in range(len(A))] for i in range(len(A))]
U = [[0 for j in range(len(A))] for i in range(len(A))]
for i in range(len(A)):
    for j in range(len(A)):
        if i<=j:
            U[i][j] += answer[i][j]
            if i == j:
                L[i][j]+=1
        else:
            L[i][j] += answer[i][j]

print("The L matrix is : ", L)
print("The U matrix is : ", U)

P = myLibrary().matrix_multi(L,U)
print("Product of L and U is : ",P)
if P == myLibrary().read_matrix("matrixA.txt"):
    print("Product is verified and it is correct!")

########################################################
# original matrix :  [[1.0, 2.0, 4.0], [3.0, 8.0, 14.0], [2.0, 6.0, 13.0]]
# The L matrix is :  [[1, 0, 0], [3.0, 1, 0], [2.0, 1.0, 1]]
# The U matrix is :  [[1.0, 2.0, 4.0], [0, 2.0, 2.0], [0, 0, 3.0]]
# Product of L and U is :  [[1.0, 2.0, 4.0], [3.0, 8.0, 14.0], [2.0, 6.0, 13.0]]
# Product is verified and it is correct!
########################################################

# Assignment 3 Question : 2
# Given below is a system of linear equations. Use LU decomposition to solve it
# by forward-backward substitution. Use either Doolittle or Crout.

# using Doolittle

B = myLibrary().read_matrix("matrixB.txt")
C = myLibrary().read_matrix("matrixC.txt")

result = LU_decomp().storeLU(B)
# print(result)
# Forward substitution: solve L * Y = C
Y = [[0] for _ in range(len(B))]
Y[0][0] = C[0][0] 

for i in range(1, len(B)):
    sum1 = 0
    for j in range(i):
        sum1 += result[i][j] * Y[j][0]
    Y[i][0] = C[i][0] - sum1            

# Back substitution: solve U * X = Y
X = [[0] for _ in range(len(B))]
X[-1][0] = Y[-1][0] / result[-1][-1]

for i in range(len(B)-2, -1, -1):
    sum2 = 0
    for j in range(i+1, len(B)):
        sum2 += result[i][j] * X[j][0]
    X[i][0] = (Y[i][0] - sum2) / result[i][i]

print("solution of the equation is : ", X)

#######################################################
# solution of the equation is :  [[-1.761817043997862], [0.8962280338740133], [4.051931404116158], 
# [-1.6171308025395421], [2.041913538501913], [0.15183248715593525]]
#######################################################