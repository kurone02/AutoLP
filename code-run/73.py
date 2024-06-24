from pulp import *

# Define the variables
num_blankets = LpVariable("NumBlankets", lowBound=0, cat='Integer')
num_sweaters = LpVariable("NumSweaters", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("GrandmotherKnittingProblem", LpMaximize)
objective = 5.50 * num_blankets + 5 * num_sweaters
problem += objective

# Define the constraints
problem += 30 * num_blankets + 20 * num_sweaters <= 200
problem += 5 * num_blankets + 4 * num_sweaters <= 40

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of blankets to knit:", value(num_blankets))
print("The number of sweaters to knit:", value(num_sweaters))
print("The maximum profit:", value(objective))
print("## end solving")