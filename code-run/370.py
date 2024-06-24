from pulp import *

# Define the decision variables
num_compact = LpVariable("NumCompact", lowBound=1000, cat='Integer')
num_midsize = LpVariable("NumMidsize", lowBound=1000, cat='Integer')
num_large = LpVariable("NumLarge", lowBound=1000, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("DorianAutoProblem", LpMaximize)

# Define the objective function
objective = 2000 * num_compact + 3000 * num_midsize + 4000 * num_large
problem += objective

# Define the constraints
problem += 1.5 * num_compact + 3 * num_midsize + 5 * num_large <= 10000
problem += 30 * num_compact + 40 * num_midsize + 25 * num_large <= 120000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of compact cars to produce:", num_compact.value())
print("The number of midsize cars to produce:", num_midsize.value())
print("The number of large cars to produce:", num_large.value())
print("The maximum profit:", objective.value())
print("## end solving")