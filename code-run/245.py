from pulp import *

# Define the decision variables
# number of ferry trips
num_ferry_trips = LpVariable("NumFerryTrips", lowBound=0, cat='Integer')
# number of light rail trips
num_light_rail_trips = LpVariable("NumLightRailTrips", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("FarmerTransportProblem", LpMinimize)

# Define the objective function
# minimize the total number of trips
objective = num_ferry_trips + num_light_rail_trips
problem += objective

# Define the constraints
# total number of boxes of corn
problem += 20 * num_ferry_trips + 15 * num_light_rail_trips >= 500
# number of light rail trips constraint
problem += num_light_rail_trips >= 4 * num_ferry_trips

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of ferry trips:", num_ferry_trips.value())
print("The number of light rail trips:", num_light_rail_trips.value())
print("The total number of trips:", objective.value())
print("## end solving")