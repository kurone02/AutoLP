from pulp import *

# Define the variables
num_molars = LpVariable("NumMolars", lowBound=45, cat='Integer')
num_canines = LpVariable("NumCanines", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("DentistProblem", LpMinimize)
objective = 3 * num_molars + 2.3 * num_canines
problem += objective

# Define the constraints
problem += 20 * num_molars + 15 * num_canines <= 3000
problem += num_canines >= 0.6 * (num_molars + num_canines)
problem += num_molars >= 45

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of molars to fill:", value(num_molars))
print("The number of canines to fill:", value(num_canines))
print("The total amount of pain killer needed:", value(objective))
print("## end solving")