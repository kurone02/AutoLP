from pulp import *

# Define the variables
num_counter_top = LpVariable("NumCounterTop", lowBound=0, cat='Integer')
num_fridge = LpVariable("NumFridge", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("IceCreamStoreProblem", LpMinimize)
objective = num_counter_top + num_fridge
problem += objective

# Define the constraints
problem += 80 * num_counter_top + 150 * num_fridge >= 1000
problem += 50 * num_counter_top + 70 * num_fridge <= 500

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of counter-top sized machines:", value(num_counter_top))
print("The number of fridge-sized machines:", value(num_fridge))
print("Total number of machines needed:", value(objective))
print("## end solving")