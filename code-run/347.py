from pulp import *

# Define the variables
num_regular_trips = LpVariable("NumRegularTrips", lowBound=0, cat='Integer')
num_speed_trips = LpVariable("NumSpeedTrips", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("MailDeliveryProblem", LpMinimize)

# Define the objective function
objective = 10 * num_regular_trips + 20 * num_speed_trips
problem += objective

# Define the constraints
problem += 20 * num_regular_trips + 30 * num_speed_trips >= 1000
problem += num_regular_trips <= 20
problem += num_speed_trips >= 0.5 * (num_regular_trips + num_speed_trips)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of regular boat trips:", num_regular_trips.value())
print("The number of speed boat trips:", num_speed_trips.value())
print("The total amount of gas consumed:", objective.value())
print("## end solving")