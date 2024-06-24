from pulp import *

# Define the decision variables
# number of truck trips
num_truck_trips = LpVariable("NumTruckTrips", lowBound=0, cat='Integer')
# number of car trips
num_car_trips = LpVariable("NumCarTrips", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("ShippingCompanyProblem", LpMinimize)

# Define the objective function
# minimize the total amount of gas consumed
objective = 20 * num_truck_trips + 15 * num_car_trips
problem += objective

# Define the constraints
# total packages transported
problem += 50 * num_truck_trips + 30 * num_car_trips >= 500
# maximum number of truck trips
problem += num_truck_trips <= 5
# at least 30% of all the trips must be made by car
problem += num_car_trips >= 0.3 * (num_truck_trips + num_car_trips)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of truck trips:", num_truck_trips.value())
print("The number of car trips:", num_car_trips.value())
print("Total amount of gas consumed:", objective.value())
print("## end solving")