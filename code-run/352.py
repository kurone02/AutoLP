from pulp import *

# Define the decision variables
num_buses = LpVariable("NumBuses", lowBound=0, cat='Integer')
num_cars = LpVariable("NumCars", lowBound=5, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("DaycareCenterProblem", LpMinimize)

# Define the objective function
# minimize the total number of vehicles
objective = num_buses + num_cars
problem += objective

# Define the constraints
# total children to pick up
problem += 9 * num_buses + 4 * num_cars >= 100
# more buses than personal cars
problem += num_buses >= num_cars
# at least 5 personal cars
problem += num_cars >= 5

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of buses:", num_buses.value())
print("The number of personal cars:", num_cars.value())
print("The total number of vehicles:", objective.value())
print("## end solving")