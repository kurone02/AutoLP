from pulp import *

# Define the variables
num_salads = LpVariable("NumSalads", lowBound=0, cat='Integer')
num_fruit_bowls = LpVariable("NumFruitBowls", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("NavyShipProblem", LpMaximize)

# Define the objective function
problem += 2 * num_salads + 8 * num_fruit_bowls

# Define the constraints
problem += 7 * num_salads + 15 * num_fruit_bowls >= 90
problem += 12 * num_salads + 3 * num_fruit_bowls >= 110
problem += num_fruit_bowls <= 0.3 * (num_salads + num_fruit_bowls)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of salads:", num_salads.value())
print("The number of fruit bowls:", num_fruit_bowls.value())
print("The total potassium intake:", (2 * num_salads.value() + 8 * num_fruit_bowls.value()))
print("## end solving")