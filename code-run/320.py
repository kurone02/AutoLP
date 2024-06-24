from pulp import *

# Define the decision variables
# number of kayak trips
num_kayak_trips = LpVariable("NumKayakTrips", lowBound=0, cat='Integer')
# number of motorboat trips
num_motorboat_trips = LpVariable("NumMotorboatTrips", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("LakeTransportationProblem", LpMinimize)

# Define the objective function
# minimize the total time needed to transport all the locals
objective = 5 * num_kayak_trips + 3 * num_motorboat_trips
problem += objective

# Define the constraints
# at least 550 locals must be moved
problem += 4 * num_kayak_trips + 5 * num_motorboat_trips >= 550
# there can be at most 25 motorboat trips
problem += num_motorboat_trips <= 25
# at least 75% of the trips should be by kayak
problem += num_kayak_trips >= 0.75 * (num_kayak_trips + num_motorboat_trips)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of kayak trips:", num_kayak_trips.value())
print("The number of motorboat trips:", num_motorboat_trips.value())
print("The total time needed to transport all the locals:", objective.value())
print("## end solving")