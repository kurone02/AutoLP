from pulp import *

# Define the variables
num_drummondville = LpVariable("NumDrummondville", lowBound=0, cat='Integer')
num_victoriaville = LpVariable("NumVictoriaville", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("CoffeeBlendProblem", LpMaximize)
objective = 5 * num_drummondville + 7 * num_victoriaville
problem += objective

# Define the constraints
problem += 600 * num_drummondville + 375 * num_victoriaville <= 24000
problem += 400 * num_drummondville + 625 * num_victoriaville <= 17000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of bags of Drummondville blend to produce:", value(num_drummondville))
print("The number of bags of Victoriaville blend to produce:", value(num_victoriaville))
print("The maximum profit:", value(objective))
print("## end solving")