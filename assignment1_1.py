# Name: Pragya Goyal  RollNo.: 2311127 
# Question 1

# Use the iterative equation xi+1 = c xi (1 − xi) to generate 10,000 random num-bers. 
# Show the correlation among them by plotting xi vs xi+k. Use seed x0 = 0.1 but choose your
# own five different c. Try various k, say 5, 10, 15, 20 etc.
import matplotlib.pyplot as plt
c = 3.98
seed = 0.1
k=15
limit = 1000
l = [seed]
for i in range(1,limit):
    l.append(c*(l[-1]*(1-l[-1])))
print("The equation is x_(i+1) = c*x_(i)*(1-x_(i))")
#print(f"{limit} random numbers with c = {c} and seed = {seed} is \n", l)
l_x = [] 
l_y = []
for i in range(limit-k):
    l_x.append(l[i])
    l_y.append(l[i+k])

plt.scatter(l_x, l_y)
plt.title(f"Correlation of random numbers with k = {k}, c = {c} and seed = {seed} is")
plt.xlabel("x_{i}")
plt.ylabel("x_{i+k}")
plt.show()

