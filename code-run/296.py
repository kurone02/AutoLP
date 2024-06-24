from pulp import *

# Define the variables
num_helicopter_trips = LpVariable("NumHelicopterTrips", lowBound=0, cat='Integer')
num_truck_trips = LpVariable("NumTruckTrips", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("FarmerProblem", LpMinimize)
objective = 5 * num_helicopter_trips + 10 * num_truck_trips
problem += objective

# Define the constraints
problem += 3 * num_helicopter_trips + 7 * num_truck_trips == 80
problem += num_truck_trips <= 8

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("Number of helicopter trips:", num_helicopter_trips.value())
print("Number of truck trips:", num_truck_trips.value())
print("Total amount of pollution produced:", objective.value())
print("## end solving")