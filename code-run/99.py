from pulp import *

# Define the variables
num_elephants = LpVariable("NumElephants", lowBound=0, cat='Integer')
num_tigers = LpVariable("NumTigers", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("SouvenirShopProblem", LpMaximize)
objective = 5 * num_elephants + 4 * num_tigers
problem += objective

# Define the constraints
problem += 50 * num_elephants + 40 * num_tigers <= 5000
problem += 20 * num_elephants + 30 * num_tigers <= 4000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of elephants made:", value(num_elephants))
print("The number of tigers made:", value(num_tigers))
print("The total profit:", value(objective))
print("## end solving")