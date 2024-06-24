from pulp import *

# Define the decision variables
# number of helicopter trips
num_helicopter_trips = LpVariable("NumHelicopterTrips", lowBound=0, cat='Integer')
# number of car trips
num_car_trips = LpVariable("NumCarTrips", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("FishTransportationProblem", LpMinimize)

# Define the objective function
# minimize the total time
objective = 40 * num_helicopter_trips + 30 * num_car_trips
problem += objective

# Define the constraints
# total number of fish transported
problem += 30 * num_helicopter_trips + 20 * num_car_trips >= 300
# maximum number of helicopter trips
problem += num_helicopter_trips <= 5
# minimum percentage of trips by car
problem += num_car_trips >= 0.6 * (num_helicopter_trips + num_car_trips)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of helicopter trips:", num_helicopter_trips.value())
print("The number of car trips:", num_car_trips.value())
print("The total time needed:", objective.value())
print("## end solving")