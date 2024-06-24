from pulp import *

# Define the variables
num_regular_truck_trips = LpVariable("NumRegularTrips", lowBound=0, cat='Integer')
num_refrigerated_truck_trips = LpVariable("NumRefrigeratedTrips", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("PotatoFarmerProblem", LpMaximize)
objective = 70 * num_regular_truck_trips + 100 * num_refrigerated_truck_trips
problem += objective

# Define the constraints
problem += 50 * num_regular_truck_trips + 70 * num_refrigerated_truck_trips <= 5000
problem += num_refrigerated_truck_trips <= num_regular_truck_trips

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of regular truck trips:", value(num_regular_truck_trips))
print("The number of refrigerated truck trips:", value(num_refrigerated_truck_trips))
print("The number of potato packages transported:", value(objective))
print("## end solving")