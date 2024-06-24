from pulp import *

# Define the decision variables
num_pigeons = LpVariable("NumPigeons", lowBound=20, cat='Integer')
num_owls = LpVariable("NumOwls", lowBound=0, cat='Integer') 

# Define the problem
problem = LpProblem("MagicSchoolProblem", LpMinimize)

# Define the objective function
objective = 3 * num_pigeons + 5 * num_owls
problem += objective

# Define the constraints
problem += num_pigeons + num_owls <= 0.4 * 100
problem += 3 * num_pigeons + 5 * num_owls <= 1000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of carrier pigeons:", num_pigeons.value())
print("The number of owls:", num_owls.value())
print("The total number of letters sent:", 2 * num_pigeons.value() + 5 * num_owls.value())
print("## end solving")