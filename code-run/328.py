from pulp import *

# Define the variables
num_smoothies = LpVariable("NumSmoothies", lowBound=0, cat='Integer')
num_bars = LpVariable("NumBars", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("DietProblem", LpMaximize)
objective = 2 * num_smoothies + 7 * num_bars
problem += objective

# Define the constraints
problem += 300 * num_smoothies + 250 * num_bars <= 2000
problem += num_bars == 2 * num_smoothies

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of smoothies:", num_smoothies.value())
print("The number of protein bars:", num_bars.value())
print("The amount of protein consumed:", objective.value())
print("## end solving")