from pulp import *

# Define the variables
num_small_trucks = LpVariable("NumSmallTrucks", lowBound=10, cat='Continuous')
num_large_trucks = LpVariable("NumLargeTrucks", lowBound=3, cat='Integer')

# Define the problem
problem = LpProblem("SnowRemovalProblem", LpMaximize)
objective = 30 * num_small_trucks + 50 * num_large_trucks
problem += objective

# Define the constraints
problem += 2 * num_small_trucks + 4 * num_large_trucks <= 60
problem += num_small_trucks == 2 * num_large_trucks

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of small trucks:", num_small_trucks.value())
print("The number of large trucks:", num_large_trucks.value())
print("The amount of snow transported:", objective.value())
print("## end solving")