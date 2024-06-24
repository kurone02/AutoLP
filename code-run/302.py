from pulp import *

# Define the decision variables
# number of boat trips
num_boat_trips = LpVariable("NumBoatTrips", lowBound=0, cat='Integer')
# number of canoe trips
num_canoe_trips = LpVariable("NumCanoeTrips", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("DuckTransportationProblem", LpMinimize)

# Define the objective function
# minimize the total time
objective = 20 * num_boat_trips + 40 * num_canoe_trips
problem += objective

# Define the constraints
# total number of ducks
problem += 10 * num_boat_trips + 8 * num_canoe_trips >= 300
# maximum number of boat trips
problem += num_boat_trips <= 12
# minimum number of canoe trips
problem += num_canoe_trips >= 0.6 * (num_boat_trips + num_canoe_trips)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of boat trips:", num_boat_trips.value())
print("The number of canoe trips:", num_canoe_trips.value())
print("The total amount of time:", objective.value())
print("## end solving")