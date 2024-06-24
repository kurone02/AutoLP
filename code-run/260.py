from pulp import *

# Define the decision variables
# number of desks
num_desks = LpVariable("NumDesks", lowBound=0, cat='Integer')
# number of drawers
num_drawers = LpVariable("NumDrawers", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("OfficeCompanyProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 100 * num_desks + 90 * num_drawers
problem += objective

# Define the constraints
# total assembly time
problem += 40 * num_desks + 30 * num_drawers <= 4000
# total sanding time
problem += 20 * num_desks + 10 * num_drawers <= 3500

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of desks:", num_desks.value())
print("The number of drawers:", num_drawers.value())
print("The total profit:", objective.value())
print("## end solving")