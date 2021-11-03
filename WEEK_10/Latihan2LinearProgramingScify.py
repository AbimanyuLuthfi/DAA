# Import Required Libraries
import numpy as np
from scipy.optimize import linprog

# Set The Inequality Constraints Matrix
# Note : The Inequality Constraints Must Be In The Form Of <=
A = np.array([[1,1], [3,4], [-1,0], [0,-1]])

# Set The Inequality Contraints Vector
b = np.array([16, 55, 0, 0])

# Set The Coefficients Of The linear Objective Function Vector
# Note : When Maximizing, Change The Signs Of the c Vector Coefficient
c = np.array([-1,-1])

# Solve Linear Programming Problem
res = linprog(c, A_ub = A, b_ub = b)

# print Results
print('Optimal value :', round(res.fun * -1, ndigits = 2),
     '\nx values :', res.x,
     '\nNumber of iterations performed :', res.nit,
     '\nStatus :', res.message)
