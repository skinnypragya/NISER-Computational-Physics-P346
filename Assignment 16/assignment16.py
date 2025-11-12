# Name : Pragya Goyal     
# Roll No : 2311127

# ------------------ Question 1 --------------
#  Use Lagrange’s interpolation formula to find the best estimate for y(6.7).

from pragyalib import datafit
import math
import matplotlib.pyplot as plt
solve = datafit()
x = [2, 3, 5, 8, 12]
y = [10, 15, 25, 40, 60]

result = solve.lagrange_interpolation(x, y, 6.7)
print("The best estimate for y(6.7) using Lagrange's interpolation is:", result)

'''
The best estimate for y(6.7) using Lagrange's interpolation is: 33.49999999999999
'''

# ------------------- Question 2 --------------
# Fit the data given in the table below with power law y = axb and exponential
# y = ae−bx models. Based on Pearson’s r^^2, determine which model gives better fit.

def power_law_fit(x, y):
    log_x = [math.log(xi) for xi in x]
    log_y = [math.log(yi) for yi in y]
    return solve.linear_regression(log_x, log_y)

def exponential_fit(x, y):
    log_y = [math.log(yi) for yi in y]
    return solve.linear_regression(x, log_y)

x_data = [2.5, 3.5, 5.0, 6.0, 7.5, 10.0, 12.5, 15.0, 17.5, 20.5]
y_data = [13.0, 11.0, 8.5, 8.2, 7.0, 6.2, 5.2, 4.8, 4.6, 4.3]

fit1 = power_law_fit(x_data, y_data)
fit2 = exponential_fit(x_data, y_data)
print("\nFitting data with Power Law model:", fit1)
print("Fitting data with Exponential model:", fit2)


# Calculating r^^2 for Power law
r2_power = solve.pearson_r_squared([math.log(xi) for xi in x_data], [math.log(yi) for yi in y_data])
print("the pearson's r^2 for power law is : ", r2_power)

# Calculating r^^2 for Exponential
r2_exponential = solve.pearson_r_squared(x_data, [math.log(yi) for yi in y_data])
print("the pearson's r^2 for exponential law is : ", r2_exponential)

y_power_fitdata = [math.exp(fit1[1]) * (xi ** fit1[0]) for xi in x_data]
y_exponential_fitdata = [math.exp(fit2[1]) * math.exp(fit2[0] * xi) for xi in x_data]

'''
the pearson's r^2 for power law is :  0.9945183457900386 (MORE ACCURATE)
the pearson's r^2 for exponential law is :  0.9017917512937711
'''

# Plotting the data and fits
plt.plot(x_data, y_data, 'o', label='Original Data')
plt.plot(x_data, y_power_fitdata, '-', label='Power Law Fit')
plt.plot(x_data, y_exponential_fitdata, '-', label='Exponential Fit')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Data Fitting with Power Law and Exponential Models')
plt.show()