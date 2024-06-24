from pulp import *

# Define the variables
num_bikes = LpVariable("NumBikes", lowBound=0, cat='Integer')
num_cars = LpVariable("NumCars", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("BanquetTransportationProblem", LpMinimize)
problem += num_bikes

# Define the constraints
problem += 3 * num_bikes + 5 * num_cars >= 500
problem += num_cars <= 0.4 * (num_bikes + num_cars)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of bikes needed:", value(num_bikes))
print("The number of cars needed:", value(num_cars))
print("The total number of vehicles used:", value(num_bikes + num_cars))
print("## end solving")