# Name : Pragya Goyal   Roll No. : 2311127
# Question 1 
#Use Runge-Kutta-4 method to solve and the following differential equation and
# compare with analytical form over the range x ∈ [0, π/5]. Use step sizes 0.1, 0.25,
# 0.45.
import math
import matplotlib.pyplot as plt
from pragyalib import solveDE
solve = solveDE()

def f1(x,y):
    return (x + y)**2

def y(x):
    return math.tan(x + math.pi/4) - x

xo2 = []
for i in range(0, 800):
    xo2.append(0 + i*0.001)
    if xo2[-1] >= math.pi/5:
        break
yo2 = [y(i) for i in xo2]

# for h = 0.1
h1 = 0.1
h2 = 0.25
h3 = 0.45
x1, y1 = solve.RK4(f1, [0, math.pi/5], h1, 1)
x2, y2 = solve.RK4(f1, [0, math.pi/5], h2, 1)
x3, y3 = solve.RK4(f1, [0, math.pi/5], h3, 1)

plt.plot(xo2, yo2, label= r"Plot of solution of DE = $ \frac{dy}{dx} = (x + y)^2 $", linestyle = 'dashed')
plt.plot(x1, y1, label= f"Plot using Runge Kutta for  h = {h1}")
plt.plot(x2, y2, label= f"Plot using Runge Kutta for  h = {h2}")
plt.plot(x3, y3, label= f"Plot using Runge Kutta for  h = {h3}")
plt.xlabel(r"Values of x in range [0, $ \pi/5 $]")
plt.ylabel("Respective values of y")
plt.legend()
plt.show()

# Question 2 
# Use RK4 to solve the damped simple harmonic oscillator using the following
# initial values and parameters over a time range [0, 40]. Plot variation of x, v and
# total energy E with time t.
# for simple harmonic oscillator
m = 1
k = 1
omega = 1
mu = 0.15
def f2(t, x, v):
    dxdt = v
    return dxdt
def f3(t, x, v):
    dvdt = -omega**2 * x -  mu * v
    return dvdt

t, x, v = solve.coupled_RK4(f2, f3, [0, 40], 0.1, 1, 0)

E = []
for i in range(len(x)):
    E.append(0.5*m*v[i]**2 + 0.5*k*x[i]**2)


plt.plot(t, x, label=r"position x vs time t", color='b')
plt.title("Solution of Differential Equation for Damped SHO")
plt.xlabel("Time t")
plt.ylabel("Position x")
plt.legend()
plt.show()

plt.plot(t, v, label=r"velocity v vs time t", color='r')
plt.title("Solution of Differential Equation for Damped SHO")
plt.xlabel("Time t")
plt.ylabel("Velocity v")
plt.legend()
plt.show()

plt.plot(t, E, label=r"Total Energy E vs time t", color='g')
plt.title("Solution of Differential Equation for Damped SHO")
plt.xlabel("Time t")
plt.ylabel("Total Energy E")
plt.legend()
plt.show()

plt.plot(x, v, label="Phase Space plot (v vs x)", color='black')
plt.title("Phase Space plot for Damped SHO")
plt.xlabel("Position x")
plt.ylabel("Velocity v")
plt.legend()
plt.show()
