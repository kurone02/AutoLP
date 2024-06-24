from pulp import *

# Define the decision variables
num_palladium_catalysts = LpVariable("NumPalladiumCatalysts", lowBound=0, cat='Integer')
num_platinum_catalysts = LpVariable("NumPlatinumCatalysts", lowBound=0, cat='Integer') 

# Define the question as a maximum or minimum problem
problem = LpProblem("CatalystProblem", LpMaximize)

# Define the objective function
problem += 5 * num_palladium_catalysts + 4 * num_platinum_catalysts

# Define the constraints
problem += 15 * num_palladium_catalysts + 20 * num_platinum_catalysts <= 450
problem += 25 * num_palladium_catalysts + 14 * num_platinum_catalysts <= 390

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of palladium-heavy catalysts:", num_palladium_catalysts.value())
print("The number of platinum-heavy catalysts:", num_platinum_catalysts.value())
print("The amount of carbon dioxide converted:", problem.objective.value())
print("## end solving")