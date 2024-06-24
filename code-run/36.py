from pulp import *

# Define the variables
num_printed_arts = LpVariable("NumPrintedArts", lowBound=0, cat='Integer')
num_paintings = LpVariable("NumPaintings", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("FramingProblem", LpMaximize)
objective = 5 * num_printed_arts + 8 * num_paintings
problem += objective

# Define the constraints
problem += 10 * num_printed_arts + 0 * num_paintings <= 150
problem += 5 * num_printed_arts + 15 * num_paintings <= 400

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of printed arts:", value(num_printed_arts))
print("The number of paintings:", value(num_paintings))
print("Total profit:", value(objective))
print("## end solving")