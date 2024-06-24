from pulp import *

# Define the decision variables
# number of taxi rides
num_taxi_rides = LpVariable("NumTaxiRides", lowBound=0, cat='Integer')
# number of company car rides
num_car_rides = LpVariable("NumCarRides", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("TransportationProblem", LpMinimize)

# Define the objective function
# minimize the total number of taxi rides
problem += num_taxi_rides

# Define the constraints
# total employees transported
problem += 2 * num_taxi_rides + 3 * num_car_rides >= 500
# maximum company car rides
problem += num_car_rides <= 0.6 * (num_taxi_rides + num_car_rides)
# minimum company car rides
problem += num_car_rides >= 30

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of taxi rides:", num_taxi_rides.value())
print("The number of company car rides:", num_car_rides.value())
print("## end solving")