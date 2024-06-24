from pulp import *

# Define the decision variables
# number of ship trips
num_ship_trips = LpVariable("NumShipTrips", lowBound=0, cat='Integer')
# number of plane trips
num_plane_trips = LpVariable("NumPlaneTrips", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("ExporterProblem", LpMinimize)

# Define the objective function
# minimize the total fuel consumed
objective = 500 * num_ship_trips + 300 * num_plane_trips
problem += objective

# Define the constraints
# total number of containers
problem += 40 * num_ship_trips + 20 * num_plane_trips >= 500
# maximum number of plane trips
problem += num_plane_trips <= 10
# minimum percentage of trips by ship
problem += num_ship_trips >= 0.5 * (num_ship_trips + num_plane_trips)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of ship trips:", num_ship_trips.value())
print("The number of plane trips:", num_plane_trips.value())
print("Total fuel consumed (liters):", objective.value())
print("## end solving")