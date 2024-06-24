from pulp import *

# Define the variables
num_tractors = LpVariable("NumTractors", lowBound=0, cat='Integer')
num_cars = LpVariable("NumCars", lowBound=0, cat='Integer')

# Define the problem as a minimum problem
problem = LpProblem("CornFarmerProblem", LpMinimize)

# Define the objective function
problem += num_tractors + num_cars

# Define the constraints
problem += 40 * num_tractors + 20 * num_cars >= 500
problem += num_cars >= 2 * num_tractors

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of tractors:", num_tractors.value())
print("The number of cars:", num_cars.value())
print("The total number of vehicles:", (num_tractors.value() + num_cars.value()))
print("## end solving")