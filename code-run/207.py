from pulp import *

# Define the decision variables
# number of van trips
num_van_trips = LpVariable("NumVanTrips", lowBound=0, cat='Integer')
# number of truck trips
num_truck_trips = LpVariable("NumTruckTrips", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("ChocolateTransportationProblem", LpMinimize)

# Define the objective function
# minimize the total number of trips
objective = num_van_trips + num_truck_trips
problem += objective

# Define the constraints
# total number of boxes transported
problem += 50 * num_van_trips + 80 * num_truck_trips >= 1500
# total cost
problem += 30 * num_van_trips + 50 * num_truck_trips <= 1000
# number of van trips must be larger than the number of truck trips
problem += num_van_trips >= num_truck_trips

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of van trips:", num_van_trips.value())
print("The number of truck trips:", num_truck_trips.value())
print("The total number of trips:", objective.value())
print("## end solving")