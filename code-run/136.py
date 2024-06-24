from pulp import *

# Define the decision variables
# number of almond croissants
num_almond = LpVariable("NumAlmond", lowBound=0, cat='Integer')
# number of pistachio croissants
num_pistachio = LpVariable("NumPistachio", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("BakeryProductionTimeMinimization", LpMinimize)

# Define the objective function
# minimize the total production time
objective = 12 * num_almond + 10 * num_pistachio
problem += objective

# Define the constraints
# total butter constraint
problem += 5 * num_almond + 3 * num_pistachio <= 600
# total flour constraint
problem += 8 * num_almond + 6 * num_pistachio <= 800
# almond croissant popularity constraint
problem += num_almond >= 3 * num_pistachio

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of almond croissants:", num_almond.value())
print("The number of pistachio croissants:", num_pistachio.value())
print("The total production time in minutes:", objective.value())
print("## end solving")