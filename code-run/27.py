from pulp import *

# Define the variables
num_AA_batteries = LpVariable("NumAA", lowBound=0, cat='Integer')
num_D_batteries = LpVariable("NumD", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("BatteryStoreProblem", LpMaximize)
objective = 0.5 * num_AA_batteries + 1 * num_D_batteries
problem += objective

# Define the constraints
problem += 1 * num_AA_batteries + 3 * num_D_batteries <= 1000
problem += num_AA_batteries <= 1000
problem += num_D_batteries <= 1000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of AA batteries to stock:", num_AA_batteries.value())
print("The number of D batteries to stock:", num_D_batteries.value())
print("Total profit:", objective.value())
print("## end solving")