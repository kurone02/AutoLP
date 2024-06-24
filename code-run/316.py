from pulp import *

# Define the decision variables
# number of Process J
num_j = LpVariable("ProcessJ", lowBound=0, cat='Integer')
# number of Process P
num_p = LpVariable("ProcessP", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("MetalExtractionProblem", LpMaximize)

# Define the objective function
# maximize the total metal extracted
objective = 5 * num_j + 9 * num_p
problem += objective

# Define the constraints
# total water used
problem += 8 * num_j + 6 * num_p <= 1500
# total pollution produced
problem += 3 * num_j + 5 * num_p <= 1350
# total processes
problem += num_j + num_p <= 1000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of Process J:", num_j.value())
print("The number of Process P:", num_p.value())
print("The total metal extracted:", objective.value())
print("## end solving")