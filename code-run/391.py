from pulp import *

# Define the decision variables
# number of model X computers
num_X = LpVariable("NumX", lowBound=0, cat='Integer')
# number of model Y computers
num_Y = LpVariable("NumY", lowBound=0, cat='Integer') 
# number of model Z computers
num_Z = LpVariable("NumZ", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("CompMaxProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 100 * num_X + 125 * num_Y + 200 * num_Z
problem += objective

# Define the constraints
# total assembly time
problem += 1 * num_X + 2 * num_Y + 3 * num_Z <= 400
# total inspection time
problem += 2 * num_X + 3 * num_Y + 4 * num_Z <= 300
# total storage space
problem += 3 * num_X + 4 * num_Y + 5 * num_Z <= 500
# at least 12 model X computers
problem += num_X >= 12
# fraction of total production made up of model Z computers
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