from pulp import *

# Define the decision variables
# number of runner deliveries
num_runner_deliveries = LpVariable("NumRunnerDeliveries", lowBound=4, cat='Integer')
# number of canoe deliveries
num_canoe_deliveries = LpVariable("NumCanoeDeliveries", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("VillageDeliveryProblem", LpMaximize)

# Define the objective function
# maximize the total amount of mail delivered
objective = 3 * num_runner_deliveries + 10 * num_canoe_deliveries
problem += objective

# Define the constraints
# at most 33% of deliveries can be by canoe
problem += num_canoe_deliveries <= 0.33 * (num_runner_deliveries + num_canoe_deliveries)
# the village can spare at most 200 total hours
problem += 4 * num_runner_deliveries + 2 * num_canoe_deliveries <= 200
# at least 4 runners must be used
problem += num_runner_deliveries >= 4

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of runner deliveries:", num_runner_deliveries.value())
print("The number of canoe deliveries:", num_canoe_deliveries.value())
print("The total amount of mail delivered:", objective.value())
print("## end solving")