from pulp import *

# Define the decision variables
# number of limousines to use
num_limousines = LpVariable("NumLimousines", lowBound=0, cat='Integer')
# number of buses to use
num_buses = LpVariable("NumBuses", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("PartyTransportationProblem", LpMinimize)

# Define the objective function
# minimize the total number of vehicles used
objective = num_limousines + num_buses
problem += objective

# Define the constraints
# total number of people to transport
problem += 12 * num_limousines + 18 * num_buses >= 400
# at least 70% of the vehicles must be limousines
problem += num_limousines >= 0.7 * (num_limousines + num_buses)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of limousines:", num_limousines.value())
print("The number of buses:", num_buses.value())
print("The total number of vehicles:", objective.value())
print("## end solving")