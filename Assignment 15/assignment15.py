# Name : Pragya Goyal 
# Roll No : 2311127

# Question 1 : 
# Equation for heat conduction in a thin, un-insulated rod of length L = 10 m is
# given by d2T/dx2 = α(T − Ta),
# where the heat transfer coefficient α = 0.01 m−2 parameterizes heat dissipated
# to the surrounding air and Ta = 20o C is the ambient temperature. If T(x =
# 0) = 40o C and T(x = L) = 200o C, solve the boundary value problem using
# Shooting Method with RK4 integrator and determine at what x the temperature
# is T = 100o C.
import matplotlib.pyplot as plt
def f1(x, T, dTdx):
    alpha = 0.01
    Ta = 20
    d2Tdx2 = alpha * (T - Ta)
    return d2Tdx2
def f2(x, T, dTdx):
    return dTdx
from pragyalib import solveDE
solve = solveDE()
L = 10
T0 = 40
TL = 200

x1, y1 = solve.shooting_RK4(10, 40, f2, f1, [0, L], 0.1, T0, TL, 10**-5)

plt.scatter(x1, y1, label="Temperature distribution along the rod")
plt.xlabel("Position along the rod (m)")
plt.ylabel("Temperature (C)")
plt.axhline(y=100, color='r', linestyle='--', label="T = 100C")
plt.legend()
plt.show()
# find the position where T = 100
for i in range(len(y1)-1):
    if (y1[i] - 100) * (y1[i+1] - 100) < 0:
        x = x1[i] + (x1[i+1] - x1[i]) * (100 - y1[i]) / (y1[i+1] - y1[i])
        print(f"The position along the rod where T = 100 celcius is approximately x = {x:.3f} m")
        break
'''
OUTPUT : 
The position along the rod where T = 100 celcius is approximately x = 4.425 m
'''
# Question 2 :
# Solve the 1-dimensional heat equation uxx = ut over a conducting bar, of length
# 2 units, kept at 0o C but is heated to 300o C at its center at time t = 0. Choose
# your ∆x and ∆t with care such that ∆t/(∆x)^2 < 0.5.
def heat_equation(L, Nx, T, Nt):
        dx = L / (Nx - 1)  # spatial step size
        dt = T / (Nt - 1)  # time step size
        
        r = dt / (dx * dx)
        if r >= 0.5:
            raise ValueError(f"Stability condition not met. dt/(dx^2) = {r:.3f} should be < 0.5")
        
        u = [[0 for _ in range(Nx)] for _ in range(Nt)]
        x = [i * dx for i in range(Nx)]
        
        # Initial conditions
        # Set temperature to 300C at the center, 0C elsewhere
        center_index = Nx // 2
        u[0][center_index] = 300

        for n in range(0, Nt-1):
            for i in range(1, Nx-1):
                u[n+1][i] = u[n][i] + r * (u[n][i+1] - 2*u[n][i] + u[n][i-1])

            u[n+1][0] = 0
            u[n+1][-1] = 0
        
        return x, u
L = 2
Nx = 21
T = 2.0
Nt = 1001
x, u = heat_equation(L, Nx, T, Nt)

time_intervals = [0, 4, 8, 10, 40, 60, 100, 1000]
for n in time_intervals:
    plt.plot(x, u[n], label=f'Time = {n * (T / (Nt - 1)):.2f} s')
plt.xlabel('Position along the rod (m)')
plt.ylabel('Temperature (C)')
plt.title('Temperature distribution along the rod over time')
plt.legend()
plt.show()
