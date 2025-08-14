# Generate pRNG having exponential distribution of the form exp(−x) from pRNG
# having uniform distribution in [0, 1). Generate at least 5,000 random numbers

# name = Pragya Goyal  Roll No.: 2311127
import matplotlib.pyplot as plt
from pragyalib import lcg
import numpy as np
limit = 10000
x = 10
a = 1103515245
c = 12345
m = 32768
f = lcg()
l1 = f.lcg_gen(limit, x, a, c, m)
L = []
L_y = []
for i in l1:
    L.append(i/m)
for x in L:
    L_y.append(-np.log(x))

plt.hist(L_y, bins=40, color='skyblue', edgecolor='black')
plt.xlabel("randomly numbers")
plt.ylabel("Frequency of random number")
plt.title("Exponential decay graph")
plt.show()