from pulp import *

# Define the variables
num_vegetable = LpVariable("NumVegetable", lowBound=0, cat='Integer')
num_fruit = LpVariable("NumFruit", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("VitaminMineralProblem", LpMinimize)

# Define the objective function
problem += 3 * num_vegetable + 5 * num_fruit

# Define the constraints
problem += 2 * num_vegetable + 4 * num_fruit >= 20
problem += 3 * num_vegetable + 1 * num_fruit >= 30

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of vegetable servings:", num_vegetable.value())
print("The number of fruit servings:", num_fruit.value())
print("The total cost:", 3 * num_vegetable.value() + 5 * num_fruit.value())
print("## end solving")