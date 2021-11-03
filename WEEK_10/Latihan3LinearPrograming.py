import pulp
# Instantiate our problem class
model = pulp.LpProblem("ProfitMaximmisingProblem", pulp.LpMaximize)
P = pulp.LpVariable('P', lowBound = 0, cat = 'Integer')
L = pulp.LpVariable('L', lowBound = 0, cat = 'Integer')

# Objective Function
model += 2 * P + 2 * L, "Profit"
#Constraints
model += 2 * P + 2 * L == 44
model += 2 * P + 2 * (P-6) == 44

# Solve our Problem
model.solve()
pulp.LpStatus[model.status]

# Print our decision variable values
print (P.varValue)
print (L.varValue)

# Print our objective function value
print (pulp.value(model.objective))
