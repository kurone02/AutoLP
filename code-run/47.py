from pulp import *

# Define the variables
num_internet = LpVariable("NumInternet", lowBound=0, cat='Integer')
num_tv = LpVariable("NumTV", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("TelecommunicationsProblem", LpMaximize)
objective = 100 * num_internet + 120 * num_tv
problem += objective

# Define the constraints
problem += 60 * num_internet + 50 * num_tv <= 7000
problem += 10 * num_internet + 20 * num_tv <= 4000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of internet services installed:", value(num_internet))
print("The number of TV services installed:", value(num_tv))
print("The total profit:", value(objective))
print("## end solving")