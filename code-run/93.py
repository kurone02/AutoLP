from pulp import *

# Define the variables
num_chairs = LpVariable("NumChairs", lowBound=0, cat='Integer')
num_dressers = LpVariable("NumDressers", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("ElmFurnitureProblem", LpMaximize)
objective = 43 * num_chairs + 52 * num_dressers
problem += objective

# Define the constraints
problem += 1.4 * num_chairs + 1.1 * num_dressers <= 17
problem += 2 * num_chairs + 3 * num_dressers <= 11

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of chairs:", value(num_chairs))
print("The number of dressers:", value(num_dressers))
print("The maximum profit:", value(objective))
print("## end solving")