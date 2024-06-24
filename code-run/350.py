from pulp import *

# Define the variables
num_chop_saws = LpVariable("NumChopSaws", lowBound=0, cat='Integer')
num_steel_cutters = LpVariable("NumSteelCutters", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("MetalWorkingShopProblem", LpMinimize)
objective = num_chop_saws + num_steel_cutters
problem += objective

# Define the constraints
problem += 25 * num_chop_saws <= 520
problem += 25 * num_chop_saws <= 400
problem += 5 * num_steel_cutters <= 520
problem += 3 * num_steel_cutters <= 400

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of chop saws:", num_chop_saws.value())
print("The number of steel cutters:", num_steel_cutters.value())
print("The total number of metal-working equipment:", objective.value())
print("## end solving")