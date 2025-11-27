# Name : Pragya Goyal
# Roll No. : 2311127

# Question 1
# Consider a box divided into two equal halves separated by a wall. At t = 0,
# there are N = 5000 particles on the left side. A hole is punched in the wall and
# one particle can pass through it at a time. All particles have equal probabilities
# of going to either sides. Graphically determine the equilibrium state (number of
# particles in left and right sides) when sufficient time ( N) has passed.
import matplotlib.pyplot as plt
import numpy as np
from pragyalib import *
random = lcg()
N = 5000
left_particles = N
right_particles = 0
left_history = [left_particles]
right_history = [right_particles]

for step in range(N):
    l = random.lcg_gen(1, 10, 1103515245, 12345, 32768)
    random_num = l[1] / 32768
    if random_num < left_particles / N:
        left_particles -= 1
        right_particles += 1
    else:
        right_particles -= 1
        left_particles += 1
    
    left_history.append(left_particles)
    right_history.append(right_particles)

print(f"Final state after {N} time steps:")
print(f"Particles on left: {left_particles}")
print(f"Particles on right: {right_particles}")
print(f"Total particles: {left_particles + right_particles}")

# Plot the equilibrium state
time_steps = range(len(left_history))
plt.plot(time_steps, left_history, 'b-', label='Left side', linewidth=2)
plt.plot(time_steps, right_history, 'r-', label='Right side', linewidth=2)
plt.xlabel('Time Steps')
plt.ylabel('Number of Particles')
plt.title('Particle Equilibrium: Two Halves with Hole in Wall')
plt.legend()
plt.show()

''' OUTPUT
Final state after 5000 time steps:
Particles on left: 2518
Particles on right: 2482
Total particles: 5000
'''

# Question 2
# Solve the following linear equation by Gauss-Seidel method to a precision of 10-6

gaussseidel = gauss_seidel()
A = myLibrary().read_matrix("matA.txt")
B = myLibrary().read_matrix("matB.txt")

sol = gaussseidel.gauss_iter(A, B, [[-1],[0], [1], [0], [3], [-2]])
print("Solutions of the equation are : ", sol[0])

''' OUTPUT
Solutions of the equation are : [[0.9999997710130514], [0.9999998045474137], [0.999999916585391], [0.9999998617941508], [0.9999998820339289], [0.99999994965483]]
'''

# Question 3 
# A spring is attached to a rigid wall at one end and a force of F = 2.5 Newton
# is applied at the other. For an arbitrary displacement x, the force acting on the
# system is F(x) = F − x exp(x). Find, using Newton-Raphson method, how far
# the spring can be stretched.

# for the displacement, solve eq x exp(x) = 2.5
import math
def f(x):
    return x*math.exp(x) - 2.5

def df(x):
    return x*math.exp(x) + math.exp(x)

root = roots().newton_raphson(f, df, 0.3, 10**-5)
print("The displacement is : ", root)

''' OUTPUT
The displacement is :  0.9585863567287043
'''

# Question 4
# A 2 meter long beam has a linear mass density λ(x) = x
# 2
# , where x is measured
# from one its ends. Find the center of mass of the beam numerically using method
# of your choice. Report answer correct up to 4 decimal places.

def g(x):
    return x**2
def gg(x):
    return x**3

I1 = integration().Simpsonsonethird([0, 2], g, 1000)
I2 = integration().Simpsonsonethird([0, 2], gg, 1000)
print("The distance of the center of mass from one end is : ", f"{I2/I1:.4f}")

''' OUTPUT
The distance of the center of mass from one end is :  1.5000
'''
# Question 7
# Fit the data given in the datafile esem4fit.txt with a quartic polynomial of the
# form a0 + a1x + a2x2 + a3x3 + a4x4
data = myLibrary().read_matrix("esem4fit.txt")
datax = [row[0] for row in data]
datay = [row[1] for row in data]
coeff = datafit().polyfit(datax, datay, [1]*26, 4)
print("The coefficients of the quartic polynomial are : ", coeff)

def h(x):
    sum = 0
    for i in range(len(coeff)):
        sum += coeff[i]*x**i
    return sum
# plot graph using coefficient
x = np.linspace(-2, 2, 100)
y = [h(i) for i in x]
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', label='fitted plot', linewidth=2)
plt.scatter(datax, datay, label='actual points', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Quartic Polynomial Fit')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

'''OUTPUT
The coefficients of the quartic polynomial are :  [0.2546295072115481, -1.1937592138092286, -0.4572554123829692, -0.8025653910658183, 0.013239427477396606]
'''

# Question 5
# An object is thrown vertically upward with velocity v0 = 10 from the ground.
# It experiences air resistances proportional to its velocity at any instant. The
# differential equation describing the motion is
# y ̈ = −γ y ̇ − g or, alternatively v
# dv
# dy = −γ v − g

# where g = 10 and γ = 0.02 in appropriate unit. Determine the maximum height
# reached by the object. Plot the variation of the velocity with height. Use RK4.
# [Hint : first determine maximum height reached without air resistance
# and then set it as upper limit for y.]

def fun1(t, y, v):
    dydt = v
    return dydt
def fun2(t, y, v):
    g = 10
    gamma = 0.02
    dvdt = -gamma*v - g
    return dvdt
t, y, v = solveDE().coupled_RK4(fun1, fun2, [0, 2], 0.01, 0, 10)

for i in range(len(v)):
    if abs(v[i]) < 10**(-2):
        print("Maximum height that object can reach is :", y[i])

plt.plot(y,v)
plt.xlabel("Displacement of object with time")
plt.ylabel("Velocity of object with time")
plt.title("Velocity vs displacement plot of the object")
plt.show()

'''OUTPUT
Maximum height that object can reach is : 4.934317509223526
'''

# Question 6
# Solve the 1-dimension heat equation uxx = ut over a metal rod of length 2 units,
# with the initial conditions,

# u(0, t) = 0oC = u(2, t) for 0 ≤ t ≤ 4
# u(x, 0) = 20 |sin (πx)|

# oC for 0 ≤ x ≤ 2

# Take number of position grid nx = 20 and time grid nt = 5000. Show the
# temperature profile across the length of the rod at time steps 0, 10, 20, 50, 100,
# 200, 500 and 1000 in a plot.

def heat_equation(L, Nx, T, Nt):
    dx = L / (Nx - 1)  # spatial step size
    dt = T / (Nt - 1)  # time step size
    r = dt / (dx * dx)
    if r >= 0.5:
        raise ValueError(f"Stability condition not met. dt/(dx^2) = {r:.3f} should be < 0.5")
    u = [[0 for _ in range(Nx)] for _ in range(Nt)]
    x = [i * dx for i in range(Nx)]
    # Initial conditions
    for i in range(Nx):
        u[0][i] = 20 * abs(math.sin(math.pi * x[i]))
    for n in range(0, Nt-1):
        for i in range(1, Nx-1):
            u[n+1][i] = u[n][i] + r * (u[n][i+1] - 2*u[n][i] + u[n][i-1])
        u[n+1][0] = 0
        u[n+1][-1] = 0
    return x, u
L = 2
Nx = 20
T = 4
Nt = 5000

# Plot temperature profiles at specified time steps
time_steps = [0, 10, 20, 50, 100, 200, 500, 1000]
x, u = heat_equation(L, Nx, T, Nt)

for s in time_steps:
    plt.plot(x, u[s], label=f'Time = {s * (T / (Nt - 1)):.3f} s')
plt.xlabel('Position along the rod (m)')
plt.ylabel('Temperature (C)')
plt.title('Temperature distribution along the rod over given time steps')
plt.legend()
plt.show()