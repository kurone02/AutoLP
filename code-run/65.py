from pulp import *

# Define the variables
num_individual_salads = LpVariable("NumIndividualSalads", lowBound=0, cat='Integer')
num_family_salads = LpVariable("NumFamilySalads", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("SaladProblem", LpMaximize)
objective = 4 * num_individual_salads + 7 * num_family_salads
problem += objective

# Define the constraints
problem += 5 * num_individual_salads + 18 * num_family_salads <= 220
problem += 2 * num_individual_salads + 6 * num_family_salads <= 150
problem += 2 * num_individual_salads + 5 * num_family_salads <= 140

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of individual salads to sell:", num_individual_salads.value())
print("The number of family-sized salads to sell:", num_family_salads.value())
print("The maximum profit:", objective.value())
print("## end solving")