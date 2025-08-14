# Determine the value of π using throwing method by choosing a quarter circle of
# unit radius in the first quadrant. Plot the value of π versus number of throws
# 20 ≤ N ≤ 2,000.
# name = Pragya Goyal  Roll No.: 2311127
import matplotlib.pyplot as plt
from pragyalib import lcg
import numpy as np
# LCG parameters
a = 1103515245
c = 12345
m = 32768
f = lcg()

x_val = []
y_val = []
limit = 20
L1 = []
L2 = []
while limit <= 10000:
    l1 = f.lcg_gen(limit, 10, a, c, m)
    l2 = f.lcg_gen(limit, 20, a, c, m)

    L1 = [n / m for n in l1]
    L2 = [n / m for n in l2]

    count = 0
    for i in range(limit):
        px = L1[i]
        py = L2[i]
        if px**2 + py**2 <= 1:
            count += 1

    pi = 4 * count / limit
    x_val.append(limit)
    y_val.append(pi)

    limit += 1

# Plot results
plt.scatter(x_val, y_val)
plt.xlabel("number of iterations")
plt.ylabel("value of pie")
plt.title("number of iterations vs value of pie plot")
plt.show()
print("average value of pi is :", np.mean(y_val))

#################################################
# average value of pi is : 3.1446228821518236

#################################################

