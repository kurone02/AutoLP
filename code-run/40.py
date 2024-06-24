from pulp import *

# Define the variables
num_display_shelves = LpVariable("NumDisplayShelves", lowBound=0, cat='Integer')
num_plant_stands = LpVariable("NumPlantStands", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("EricProblem", LpMaximize)
objective = 55 * num_display_shelves + 45 * num_plant_stands
problem += objective

# Define the constraints
problem += 25 * num_display_shelves + 20 * num_plant_stands <= 350
problem += 20 * num_display_shelves + 10 * num_plant_stands <= 600

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of display shelves to manufacture:", value(num_display_shelves))
print("The number of plant stands to manufacture:", value(num_plant_stands))
print("Total profit:", value(objective))
print("## end solving")