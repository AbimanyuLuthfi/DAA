import pulp
# Instantiate our problem class
model = pulp.LpProblem("ProfitMaximmisingProblem", pulp.LpMaximize)
X = pulp.LpVariable('X', lowBound = 0, cat = 'Integer')
Y = pulp.LpVariable('Y', lowBound = 0, cat = 'Integer')

# Objective Function
model += 2 * X + 6 * Y, "Profit"
#Constraints
model += 3 * X + 4 * Y == 11000
model += 1 * X + 7 * Y == 15000

# Solve our Problem
model.solve()
pulp.LpStatus[model.status]

# Print our decision variable values
print (X.varValue)
print (Y.varValue)

# Print our objective function value
print (pulp.value(model.objective))
