from pulp import *

# Define the decision variables
# number of submarine trips
num_submarine_trips = LpVariable("SubmarineTrips", lowBound=0, cat='Integer')
# number of boat trips
num_boat_trips = LpVariable("BoatTrips", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("TropicalCityMailProblem", LpMinimize)

# Define the objective function
# minimize the total amount of gas used
objective = 30 * num_submarine_trips + 25 * num_boat_trips
problem += objective

# Define the constraints
# total number of pieces of mail
problem += 100 * num_submarine_trips + 80 * num_boat_trips >= 1000
# maximum number of submarine trips
problem += num_submarine_trips <= 6
# minimum percentage of trips by boat
problem += num_boat_trips >= 0.5 * (num_submarine_trips + num_boat_trips)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of submarine trips:", num_submarine_trips.value())
print("The number of boat trips:", num_boat_trips.value())
print("The total amount of gas used:", objective.value())
print("## end solving")