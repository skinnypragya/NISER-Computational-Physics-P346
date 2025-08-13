# Name: Pragya Goyal  RollNo.: 2311127 
# Question 2

# Write your own LCG random generator with the following set of parameters
# a = 1103515245, c = 12345, m = 32768 and again check for correlation by
# plotting for k = 5.

import matplotlib.pyplot as plt
from pragyalib import lcg

limit = 3400
k = 5

n1 = lcg()
l = n1.lcg_gen(limit, 10,1103515245,12345, 32768)
print("Random numbers are \n", l)

l_x = [] 
l_y = []
for i in range(limit - k):
    l_x.append(l[i])
    l_y.append(l[i+k])

plt.scatter(l_x, l_y)
plt.title(f"Correlation of random numbers with k = {k}")
plt.xlabel("x_{i}")
plt.ylabel("x_{i+k}")
plt.show()