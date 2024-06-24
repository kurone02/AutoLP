from pulp import *

# Define the decision variables
# number of small wagons
num_small_wagons = LpVariable("NumSmallWagons", lowBound=0, cat='Integer')
# number of large wagons
num_large_wagons = LpVariable("NumLargeWagons", lowBound=10, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("OreMiningProblem", LpMinimize)

# Define the objective function
# minimize the total number of wagons
objective = num_small_wagons + num_large_wagons
problem += objective

# Define the constraints
# total ore
problem += 20 * num_small_wagons + 50 * num_large_wagons >= 2000
# small wagons constraint
problem += num_small_wagons >= 2 * num_large_wagons

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of small wagons:", num_small_wagons.value())
print("The number of large wagons:", num_large_wagons.value())
print("The total number of wagons needed:", objective.value())
print("## end solving")