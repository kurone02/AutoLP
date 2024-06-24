from pulp import *

# Define the variables
num_consoles = LpVariable("NumConsoles", lowBound=20, upBound=50, cat='Integer')
num_discs = LpVariable("NumDiscs", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("VideoGameStoreProblem", LpMaximize)

# Define the objective function
objective = 200 * num_consoles + 30 * num_discs
problem += objective

# Define the constraints
problem += 300 * num_consoles <= 30000
problem += 30 * num_discs <= 30000
problem += num_discs <= 5 * num_consoles

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of consoles sold:", num_consoles.value())
print("The number of discs sold:", num_discs.value())
print("Maximum profit:", objective.value())
print("## end solving")