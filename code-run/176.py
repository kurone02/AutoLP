from pulp import *

# Define the decision variables
num_X = LpVariable("NumModelX", lowBound=0, cat='Integer')
num_Y = LpVariable("NumModelY", lowBound=0, cat='Integer')
num_Z = LpVariable("NumModelZ", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("CompMaxProblem", LpMaximize)

# Define the objective function
objective = 100 * num_X + 125 * num_Y + 200 * num_Z
problem += objective

# Define the constraints
problem += 1 * num_X + 2 * num_Y + 3 * num_Z <= 400
problem += 2 * num_X + 3 * num_Y + 4 * num_Z <= 300
problem += 3 * num_X + 4 * num_Y + 5 * num_Z <= 500
problem += num_X >= 12
problem += num_Z <= 0.25 * (num_X + num_Y + num_Z)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of model X computers to produce:", num_X.value())
print("The number of model Y computers to produce:", num_Y.value())
print("The number of model Z computers to produce:", num_Z.value())
print("The maximum profit:", objective.value())
print("## end solving")