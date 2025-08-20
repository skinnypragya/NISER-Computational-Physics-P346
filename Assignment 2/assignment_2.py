# Name : Pragya Goyal  RollNo.: 2311127

# Assignment 2 Question: 1
# Prepare a library routine for Gauss-Jordan elimination method using row pivoting
# and check with the system of equations for three variables, matrixA and matrixB

from pragyalib import myLibrary, gauss_jordan
mat1 = myLibrary().read_matrix("matrixA.txt")
mat2 = myLibrary().read_matrix("matrixB.txt")
answer = gauss_jordan().jordan(mat1,mat2)
print("value of x is ", answer[0][-1])
print("value of y is ", answer[1][-1])
print("value of x is ", answer[2][-1])

############################################
# value of x is  -2.0
# value of y is  -2.0
# value of x is  1.0
############################################

# Assignment 2 Question: 2
# Given below is a system of linear equations. Use Gauss-Jordon to solve it. matrixC and matrixD

mat3 = myLibrary().read_matrix("matrixC.txt")
mat4 = myLibrary().read_matrix("matrixD.txt")
solve = gauss_jordan().jordan(mat3,mat4)
for i in range(len(mat3)):
    print(f"value of a_{i+1} is ", solve[i][-1])

#################################################
# value of a_1 is  -1.7618170439978567
# value of a_2 is  0.8962280338740136
# value of a_3 is  4.051931404116157
# value of a_4 is  -1.6171308025395428
# value of a_5 is  2.041913538501914
# value of a_6 is  0.15183248715593495
#################################################