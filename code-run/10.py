from pulp import *

# Define the decision variables
hours_north = LpVariable("HoursNorth", lowBound=0, cat='Continuous')
hours_south = LpVariable("HoursSouth", lowBound=0, cat='Continuous') 

# Define the problem
problem = LpProblem("TomDesignsProblem", LpMinimize)

# Define the objective function
problem += 200 * hours_north + 400 * hours_south

# Define the constraints
problem += 20 * hours_north >= 75
problem += 15 * hours_north >= 30
problem += 10 * hours_north >= 40
problem += 30 * hours_south >= 75
problem += 25 * hours_south >= 30
problem += 30 * hours_south >= 40

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("Number of hours the north factory operates:", value(hours_north))
print("Number of hours the south factory operates:", value(hours_south))
print("Total cost of operation:", value(problem.objective))
print("## end solving")