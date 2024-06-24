from pulp import *

# Define the variables
num_large_planes = LpVariable("NumLargePlanes", lowBound=0, cat='Integer')
num_small_planes = LpVariable("NumSmallPlanes", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("CarShippingProblem", LpMinimize)

# Define the objective function
problem += num_large_planes + num_small_planes

# Define the constraints
problem += 30 * num_large_planes + 10 * num_small_planes >= 300
problem += num_large_planes <= num_small_planes

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of large planes:", num_large_planes.value())
print("The number of small planes:", num_small_planes.value())
print("The total number of planes:", (num_large_planes.value() + num_small_planes.value()))
print("## end solving")