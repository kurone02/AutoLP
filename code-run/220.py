from pulp import *

# Define the variables
num_bus_trips = LpVariable("NumBusTrips", lowBound=0, cat='Integer')
num_car_trips = LpVariable("NumCarTrips", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("MonkeyTransportationProblem", LpMinimize)

# Define the objective function
problem += 30 * num_bus_trips + 15 * num_car_trips

# Define the constraints
problem += 20 * num_bus_trips + 6 * num_car_trips >= 300
problem += num_bus_trips <= 10
problem += num_car_trips >= 0.6 * (num_bus_trips + num_car_trips)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of bus trips:", num_bus_trips.value())
print("The number of car trips:", num_car_trips.value())
print("The total time required to transport the monkeys (minutes):", value(problem.objective))
print("## end solving")