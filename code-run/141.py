from pulp import *

# Define the variables
num_regular_vans = LpVariable("NumRegularVans", lowBound=0, cat='Integer')
num_hybrid_vans = LpVariable("NumHybridVans", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("ShippingCompanyProblem", LpMinimize)
objective = num_regular_vans + num_hybrid_vans
problem += objective

# Define the constraints
problem += 500 * num_regular_vans + 300 * num_hybrid_vans >= 20000
problem += 200 * num_regular_vans + 100 * num_hybrid_vans <= 7000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of regular vans:", value(num_regular_vans))
print("The number of hybrid vans:", value(num_hybrid_vans))
print("## end solving")