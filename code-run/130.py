from pulp import *

# Define the decision variables
# number of seasonal removers
num_seasonal_removers = LpVariable("NumSeasonalRemovers", lowBound=0, cat='Integer')
# number of permanent removers
num_permanent_removers = LpVariable("NumPermanentRemovers", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("SnowRemoverProblem", LpMinimize)

# Define the objective function
# minimize the total number of snow removers
objective = num_seasonal_removers + num_permanent_removers
problem += objective

# Define the constraints
# total hours of snow remover labor
problem += 6 * num_seasonal_removers + 10 * num_permanent_removers >= 300
# total cost
problem += 120 * num_seasonal_removers + 250 * num_permanent_removers <= 6500

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of seasonal removers:", num_seasonal_removers.value())
print("The number of permanent removers:", num_permanent_removers.value())
print("The total number of snow removers:", objective.value())
print("## end solving")