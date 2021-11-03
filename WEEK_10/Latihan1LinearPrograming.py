import pulp
# Instantiate our problem class
model = pulp.LpProblem("ProfitMaximmisingProblem", pulp.LpMaximize)
X = pulp.LpVariable('X', lowBound = 0, cat = 'Integer')
Y = pulp.LpVariable('Y', lowBound = 0, cat = 'Integer')

# Objective Function
model += 5000 * X + 2500 * Y, "Profit"
#Constraints
model += 4 * X + 3 * Y == 34
model += 5 * X + 1 * Y == 37

# Solve our Problem
model.solve()
pulp.LpStatus[model.status]

# Print our decision variable values
print (X.varValue)
print (Y.varValue)

# Print our objective function value
print (pulp.value(model.objective))
