from pulp import *

# Define the decision variables
num_trips_new = LpVariable("NumTripsNew", lowBound=0, cat='Integer')
num_trips_old = LpVariable("NumTripsOld", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("ToyStoreDelivery", LpMinimize)

# Define the objective function
# minimize the total amount of diesel used
objective = 30 * num_trips_new + 40 * num_trips_old
problem += objective

# Define the constraints
# total gifts delivered
problem += 50 * num_trips_new + 70 * num_trips_old >= 1000
# maximum trips by the new company
problem += num_trips_new <= 15
# at least 40% of all trips must be made by the old company
problem += num_trips_old >= 0.4 * (num_trips_new + num_trips_old)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of trips by the new company:", num_trips_new.value())
print("The number of trips by the old company:", num_trips_old.value())
print("The total amount of diesel used:", objective.value())
print("## end solving")