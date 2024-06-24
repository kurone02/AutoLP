from pulp import *

# Define the decision variables
num_rice_servings = LpVariable("NumRiceServings", lowBound=0, cat='Integer')
num_kebab_servings = LpVariable("NumKebabServings", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("DietProblem", LpMinimize)
objective = 3 * num_rice_servings + 2 * num_kebab_servings
problem += objective

# Define the constraints
problem += 300 * num_rice_servings + 200 * num_kebab_servings >= 2200
problem += 4.5 * num_rice_servings + 4 * num_kebab_servings >= 30

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of rice servings:", value(num_rice_servings))
print("The number of kebab servings:", value(num_kebab_servings))
print("The total cost of the diet:", value(objective))
print("## end solving")