from pulp import *

# Define the decision variables
num_model_X = LpVariable("NumModelX", lowBound=12, cat='Integer')
num_model_Y = LpVariable("NumModelY", lowBound=0, cat='Integer')
num_model_Z = LpVariable("NumModelZ", lowBound=0, cat='Integer')

# Define the question as a minimum or maximum problem
problem = LpProblem("CompMaxProfitMaximization", LpMaximize)

# Define the objective function
objective = 100 * num_model_X + 125 * num_model_Y + 200 * num_model_Z
problem += objective

# Define the constraints
problem += 1 * num_model_X + 2 * num_model_Y + 3 * num_model_Z <= 400
problem += 2 * num_model_X + 3 * num_model_Y + 4 * num_model_Z <= 300
problem += 3 * num_model_X + 4 * num_model_Y + 5 * num_model_Z <= 500
problem += num_model_Z <= 0.25 * (num_model_X + num_model_Y + num_model_Z)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of model X computers to produce:", num_model_X.value())
print("The number of model Y computers to produce:", num_model_Y.value())
print("The number of model Z computers to produce:", num_model_Z.value())
print("The maximum profit:", objective.value())
print("## end solving")