from pulp import *

# Define the decision variables
num_large_units = LpVariable("NumLargeUnits", lowBound=0, cat='Integer')
num_small_units = LpVariable("NumSmallUnits", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("MovieProductionProblem", LpMinimize)

# Define the objective function
problem += 2 * num_large_units + 1 * num_small_units

# Define the constraints
problem += 6 * num_large_units + 2 * num_small_units >= 80
problem += num_small_units >= 5
problem += num_large_units >= 0.75 * (num_large_units + num_small_units)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of large mobile production units:", num_large_units.value())
print("The number of small mobile production units:", num_small_units.value())
print("The total number of parking spots required:", (2 * num_large_units.value() + 1 * num_small_units.value()))
print("## end solving")