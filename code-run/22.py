from pulp import *

# Define the decision variables
# number of train trips
num_train_trips = LpVariable("NumTrainTrips", lowBound=0, cat='Integer')
# number of truck trips
num_truck_trips = LpVariable("NumTruckTrips", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("FarmProblem", LpMaximize)

# Define the objective function
# maximize the total number of chickens that can be transported
objective = 500 * num_train_trips + 300 * num_truck_trips
problem += objective

# Define the constraints
# total cost
problem += 100 * num_train_trips + 80 * num_truck_trips <= 2000
# the number of train trips cannot exceed the number of truck trips
problem += num_train_trips <= num_truck_trips

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of train trips:", num_train_trips.value())
print("The number of truck trips:", num_truck_trips.value())
print("The number of chickens transported:", objective.value())
print("## end solving")