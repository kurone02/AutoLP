from pulp import *

# Define the variables
num_small_crates = LpVariable("NumSmallCrates", lowBound=5, cat='Integer')
num_large_crates = LpVariable("NumLargeCrates", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("BananaCompanyProblem", LpMaximize)
objective = num_small_crates + num_large_crates
problem += objective

# Define the constraints
problem += 20 * num_small_crates + 50 * num_large_crates <= 500
problem += num_large_crates >= 1.5 * num_small_crates
problem += num_small_crates >= 5

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of small crates:", value(num_small_crates))
print("The number of large crates:", value(num_large_crates))
print("The total number of crates produced:", value(objective))
print("## end solving")