from pulp import *

# Define the variables
num_vans = LpVariable("NumVans", lowBound=0, cat='Integer')
num_cars = LpVariable("NumCars", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("VoterTransportationProblem", LpMinimize)
problem += num_cars

# Define the constraints
problem += 6 * num_vans + 3 * num_cars >= 200
problem += num_vans <= 0.3 * (num_vans + num_cars)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of vans:", num_vans.value())
print("The number of cars:", num_cars.value())
print("## end solving")