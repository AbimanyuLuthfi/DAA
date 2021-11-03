import pulp

# Instantiate our problem class
model = pulp.LpProblem("ProfitMaximmisingProblem", pulp.LpMaximize)

A = pulp.LpVariable('A', lowBound = 0, cat = 'Integer')
B = pulp.LpVariable('B', lowBound = 0, cat = 'Integer')

# Objective Function
model += 5000 * A + 2500 * B, "Profit"
#Constraints
model += 3 * A + 2 * B <= 20
model += 4 * A + 3 * B <= 30
model += 4 * A + 3 * B <= 44

# Solve our Problem
model.solve()
pulp.LpStatus[model.status]

# Print our decision variable values
print (A.varValue)
print (B.varValue)

# Print our objective function value
print (pulp.value(model.objective))
