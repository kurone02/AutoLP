from pulp import *

# Define the problem
prob = LpProblem("ProductionScheduling", LpMinimize)

# Define the data
products = ['A', 'B', 'C']
machines = [1, 2, 3]
cost = {
    'A': [0.80, 1.40, 0.80],
    'B': [1.30, 1.30, 0.80],
    'C': [0.70, 1.50, 1.20]
}
order = {
    'A': 1750,
    'B': 500,
    'C': 1100
}
capacity = {
    1: 1550,
    2: 1450,
    3: 1150
}

# Define the variables
x = LpVariable.dicts("x", (products, machines), lowBound=0, cat='Integer')

# Define the objective function
prob += lpSum([x[i][j] * cost[i][k] for i in products for j in machines for k in machines if j == k])

# Define the constraints
for i in products:
    prob += lpSum([x[i][j] for j in machines]) == order[i]

for j in machines:
    prob += lpSum([x[i][j] for i in products]) <= capacity[j]

# Solve the problem
prob.solve()

# Output the answer
print("## start solving")
for j in machines:
    for i in products:
        print(f"The production units for {i} on machine {j}:", value(x[i][j]))
print("The minimum production cost:", value(prob.objective))
print("## end solving")