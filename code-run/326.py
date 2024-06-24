from pulp import *

# Define the variables
num_invivo = LpVariable("NumInvivo", lowBound=0, cat='Integer')
num_exvivo = LpVariable("NumExvivo", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("ResearcherExperiments", LpMinimize)
objective = 2 * num_invivo + 3 * num_exvivo
problem += objective

# Define the constraints
problem += 30 * num_invivo + 45 * num_exvivo <= 400
problem += 60 * num_invivo + 30 * num_exvivo <= 500

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of in-vivo experiments:", value(num_invivo))
print("The number of ex-vivo experiments:", value(num_exvivo))
print("Total radiation received:", value(objective))
print("## end solving")