from pulp import *

# Define the decision variables
# number of hours the northern factory should run
num_hours_north = LpVariable("NumHoursNorth", lowBound=0, cat='Integer')
# number of hours the western factory should run
num_hours_west = LpVariable("NumHoursWest", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("ClinicalFirmProblem", LpMinimize)

# Define the objective function
# minimize the total time needed
objective = num_hours_north + num_hours_west
problem += objective

# Define the constraints
# total amount of plastic
problem += 40 * num_hours_north + 35 * num_hours_west <= 60000
# total amount of anti-itch injections
problem += 800 * num_hours_north + 650 * num_hours_west >= 800000
# total amount of topical cream
problem += 700 * num_hours_north + 750 * num_hours_west >= 700000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of hours the northern factory should run:", num_hours_north.value())
print("The number of hours the western factory should run:", num_hours_west.value())
print("The total time needed:", objective.value())
print("## end solving")