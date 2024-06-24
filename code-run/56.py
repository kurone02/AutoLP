from pulp import *

# Define the variables
num_servings_milk = LpVariable("NumServingsMilk", lowBound=0, cat='Integer')
num_servings_cheese = LpVariable("NumServingsCheese", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("DietProblem", LpMinimize)
objective = 2 * num_servings_milk + 4 * num_servings_cheese
problem += objective

# Define the constraints
problem += 10 * num_servings_milk + 8 * num_servings_cheese >= 100
problem += 5 * num_servings_milk + 6 * num_servings_cheese >= 80

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of servings of milk:", num_servings_milk.value())
print("The number of servings of cheese:", num_servings_cheese.value())
print("Total cost:", objective.value())
print("## end solving")