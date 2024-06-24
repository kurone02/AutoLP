from pulp import *

# Define the decision variables
num_model_X = LpVariable("NumModelX", lowBound=12, cat='Integer')
num_model_Y = LpVariable("NumModelY", lowBound=0, cat='Integer')
num_model_Z = LpVariable("NumModelZ", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("CompMaxProblem", LpMaximize)

# Define the objective function
problem += 100 * num_model_X + 125 * num_model_Y + 200 * num_model_Z

# Define the constraints
problem += 1 * num_model_X + 2 * num_model_Y + 3 * num_model_Z <= 400
problem += 2 * num_model_X + 3 * num_model_Y + 4 * num_model_Z <= 300
problem += 3 * num_model_X + 4 * num_model_Y + 5 * num_model_Z <= 500
problem += 0.25 * (num_model_X + num_model_Y + num_model_Z) >= num_model_Z

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of model X computers to produce:", value(num_model_X))
print("The number of model Y computers to produce:", value(num_model_Y))
print("The number of model Z computers to produce:", value(num_model_Z))
print("The maximum profit:", value(problem.objective))
print("## end solving")