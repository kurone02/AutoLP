from pulp import *

# Define the decision variables
# number of plane trips
num_plane_trips = LpVariable("NumPlaneTrips", lowBound=0, cat='Integer')
# number of truck trips
num_truck_trips = LpVariable("NumTruckTrips", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("TireTransportationProblem", LpMinimize)

# Define the objective function
# minimize the total number of trips
objective = num_plane_trips + num_truck_trips
problem += objective

# Define the constraints
# total number of tires to transport
problem += 10 * num_plane_trips + 6 * num_truck_trips >= 200
# total cost of transport
problem += 1000 * num_plane_trips + 700 * num_truck_trips <= 22000
# number of plane trips cannot exceed the number of truck trips
problem += num_plane_trips <= num_truck_trips

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of plane trips:", num_plane_trips.value())
print("The number of truck trips:", num_truck_trips.value())
print("The total number of trips:", objective.value())
print("## end solving")