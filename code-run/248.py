from pulp import *

# Define the decision variables
# number of small crates
num_small_crates = LpVariable("NumSmallCrates", lowBound=0, cat='Integer')
# number of large crates
num_large_crates = LpVariable("NumLargeCrates", lowBound=10, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("GrapeFarmerProblem", LpMaximize)

# Define the objective function
# maximize the total number of grapes transported
objective = 200 * num_small_crates + 500 * num_large_crates
problem += objective

# Define the constraints
# small crates available
problem += num_small_crates <= 100
# large crates available
problem += num_large_crates <= 50
# at least 10 large crates used
problem += num_large_crates >= 10
# total crates used
problem += num_small_crates + num_large_crates <= 60
# 3 times as many small crates used as large crates
problem += num_small_crates >= 3 * num_large_crates

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of small crates used:", num_small_crates.value())
print("The number of large crates used:", num_large_crates.value())
print("The total number of grapes transported:", objective.value())
print("## end solving")