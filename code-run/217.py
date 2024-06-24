from pulp import *

# Define the decision variables
# number of truck trips
num_truck_trips = LpVariable("NumTruckTrips", lowBound=0, cat='Integer')
# number of van trips
num_van_trips = LpVariable("NumVanTrips", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("MeatShopShipmentProblem", LpMinimize)

# Define the objective function
# minimize the total number of trips
objective = num_truck_trips + num_van_trips
problem += objective

# Define the constraints
# total number of patties
problem += 1000 * num_truck_trips + 500 * num_van_trips >= 50000
# total cost
problem += 300 * num_truck_trips + 100 * num_van_trips <= 12500
# number of trucks not exceeding vans
problem += num_truck_trips <= num_van_trips

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of truck trips:", num_truck_trips.value())
print("The number of van trips:", num_van_trips.value())
print("The total number of trips:", objective.value())
print("## end solving")