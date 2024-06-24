from pulp import *

# Define the decision variables
num_days_north = LpVariable("NumDaysNorth", lowBound=0, cat='Integer')
num_days_south = LpVariable("NumDaysSouth", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("ThunderWoodProblem", LpMinimize)

# Define the objective function
problem += 450 * num_days_north + 550 * num_days_south

# Define the constraints
problem += 5 * num_days_north + 6 * num_days_south >= 25
problem += 5 * num_days_north + 4 * num_days_south >= 15
problem += 4 * num_days_north + 6 * num_days_south >= 30

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("Number of days to run north side operation:", num_days_north.value())
print("Number of days to run south side operation:", num_days_south.value())
print("Total operation cost:", problem.objective.value())
print("## end solving")