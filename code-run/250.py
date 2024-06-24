from pulp import *

# Define the decision variables
num_helicopter_trips = LpVariable("NumHelicopterTrips", lowBound=0, cat='Integer')
num_bus_trips = LpVariable("NumBusTrips", lowBound=0, cat='Integer')

# Define the question as a maximum or minimum problem
problem = LpProblem("PatientTransportationProblem", LpMinimize)

# Define the objective function
objective = 1 * num_helicopter_trips + 3 * num_bus_trips
problem += objective

# Define the constraints
problem += 5 * num_helicopter_trips + 8 * num_bus_trips >= 120
problem += num_helicopter_trips >= 0.3 * (num_helicopter_trips + num_bus_trips)
problem += num_bus_trips <= 10

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of helicopter trips:", num_helicopter_trips.value())
print("The number of bus trips:", num_bus_trips.value())
print("The total time to transport the patients:", objective.value())
print("## end solving")