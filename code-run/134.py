from pulp import *

# Define the variables
num_small_containers = LpVariable("NumSmallContainers", lowBound=0, cat='Integer')
num_large_containers = LpVariable("NumLargeContainers", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("PasteProduction", LpMaximize)

# Define the objective function
problem += 20 * num_small_containers + 30 * num_large_containers

# Define the constraints
problem += 10 * num_small_containers + 20 * num_large_containers <= 500
problem += 15 * num_small_containers + 20 * num_large_containers <= 700

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of small containers:", num_small_containers.value())
print("The number of large containers:", num_large_containers.value())
print("The amount of paste produced:", (20 * num_small_containers.value() + 30 * num_large_containers.value()))
print("## end solving")