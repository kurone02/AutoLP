from pulp import *

# Define the decision variables
# number of new model furnaces
num_new_model = LpVariable("NumNewModel", lowBound=5, cat='Integer')
# number of old model furnaces
num_old_model = LpVariable("NumOldModel", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("FurnacePurchaseProblem", LpMinimize)

# Define the objective function
# minimize the total number of furnaces
objective = num_new_model + num_old_model
problem += objective

# Define the constraints
# total number of apartments heated by the furnaces
problem += 10 * num_new_model + 15 * num_old_model >= 200
# total amount of electricity consumed by the furnaces
problem += 200 * num_new_model + 250 * num_old_model <= 3500
# at most 35% of the furnaces can be the old model
problem += num_old_model <= 0.35 * (num_new_model + num_old_model)
# at least 5 new model furnaces should be used
problem += num_new_model >= 5

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of new model furnaces:", num_new_model.value())
print("The number of old model furnaces:", num_old_model.value())
print("The total number of furnaces:", objective.value())
print("## end solving")