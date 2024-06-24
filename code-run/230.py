from pulp import *

# Define the decision variables
# number of bus trips
num_bus_trips = LpVariable("BusTrips", lowBound=0, cat='Integer')
# number of car trips
num_car_trips = LpVariable("CarTrips", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("ChickenTransportationProblem", LpMinimize)

# Define the objective function
# minimize the total time taken to transport the chicken
objective = 2 * num_bus_trips + 1.5 * num_car_trips
problem += objective

# Define the constraints
# total number of chicken transported
problem += 100 * num_bus_trips + 40 * num_car_trips == 1200
# maximum number of bus trips
problem += num_bus_trips <= 10
# at least 60% of the trips must be by car
problem += num_car_trips >= 0.6 * (num_bus_trips + num_car_trips)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of bus trips:", num_bus_trips.value())
print("The number of car trips:", num_car_trips.value())
print("The total time taken to transport the chicken:", objective.value())
print("## end solving")