from pulp import *

# Define the decision variables
# number of packages of fish meat
num_fish = LpVariable("NumFish", lowBound=0, cat='Integer')
# number of packages of shrimp meat
num_shrimp = LpVariable("NumShrimp", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("SeafoodFactoryProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 7 * num_fish + 3 * num_shrimp
problem += objective

# Define the constraints
# total time in the weight checking machine
problem += 3 * num_fish + 1.5 * num_shrimp <= 1200
# total time in the packaging inspection machine
problem += 15 * num_fish + 7 * num_shrimp <= 1200

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of packages of fish meat:", num_fish.value())
print("The number of packages of shrimp meat:", num_shrimp.value())
print("The maximum profit:", objective.value())
print("## end solving")