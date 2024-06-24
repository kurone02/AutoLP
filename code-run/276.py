from pulp import *

# Define the variables
num_regular_tacos = LpVariable("NumRegularTacos", lowBound=0, cat='Integer')
num_deluxe_tacos = LpVariable("NumDeluxeTacos", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("TacoStandProblem", LpMaximize)
objective = 2.50 * num_regular_tacos + 3.55 * num_deluxe_tacos
problem += objective

# Define the constraints
problem += num_regular_tacos <= 50
problem += num_deluxe_tacos <= 40
problem += num_regular_tacos + num_deluxe_tacos <= 70

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of regular tacos:", value(num_regular_tacos))
print("The number of deluxe tacos:", value(num_deluxe_tacos))
print("The maximum profit:", value(objective))
print("## end solving")