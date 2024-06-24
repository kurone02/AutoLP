from pulp import *

# Define the problem
prob = LpProblem("ProductionScheduling", LpMinimize)

# Define the variables
products = ['A', 'B', 'C']
machines = [1, 2, 3]
demand = {'A': 1750, 'B': 500, 'C': 1100}
capacity = {1: 1550, 2: 1450, 3: 1150}
cost = {('A', 1): 0.80, ('A', 2): 1.40, ('A', 3): 0.80,
        ('B', 1): 1.30, ('B', 2): 1.30, ('B', 3): 0.80,
        ('C', 1): 0.70, ('C', 2): 1.50, ('C', 3): 1.20}

x = LpVariable.dicts("production", ((i, j) for i in products for j in machines), 0)

# Define the objective function
prob += lpSum([cost[(i, j)] * x[(i, j)] for i in products for j in machines])

# Define the constraints
for i in products:
    prob += lpSum([x[(i, j)] for j in machines]) == demand[i]

for j in machines:
    prob += lpSum([x[(i, j)] for i in products]) <= capacity[j]

# Solve the problem
prob.solve()

# Output the answer
print("## start solving")
for v in prob.variables():
    print(v.name, "=", v.varValue)
print("The minimum production cost:", value(prob.objective))
print("## end solving")