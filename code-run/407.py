from pulp import *

# Define the variables
num_product1 = LpVariable("NumProduct1", lowBound=0, cat='Integer')
num_product2 = LpVariable("NumProduct2", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("ManufacturerProblem", LpMaximize)
objective = 2 * num_product1 + 5 * num_product2 - 10 * num_product1 - 20 * num_product2
problem += objective

# Define the constraints
problem += 3 * num_product1 + 6 * num_product2 <= 120

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of units of product 1 to produce:", num_product1.value())
print("The number of units of product 2 to produce:", num_product2.value())
print("The total profit:", value(objective))
print("## end solving")