from pulp import *

# Define the variables
num_tuna_sandwiches = LpVariable("NumTunaSandwiches", lowBound=0, cat='Integer')
num_chicken_sandwiches = LpVariable("NumChickenSandwiches", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("WeightGainProblem", LpMinimize)
objective = 5 * num_tuna_sandwiches + 7 * num_chicken_sandwiches
problem += objective

# Define the constraints
problem += 20 * num_tuna_sandwiches + 25 * num_chicken_sandwiches >= 100
problem += 25 * num_tuna_sandwiches + 15 * num_chicken_sandwiches >= 150

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of tuna salad sandwiches:", num_tuna_sandwiches.value())
print("The number of chicken salad sandwiches:", num_chicken_sandwiches.value())
print("The total cost:", objective.value())
print("## end solving")