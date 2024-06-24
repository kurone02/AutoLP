from pulp import *

# Define the decision variables
# number of cars
num_cars = LpVariable("NumCars", lowBound=0, cat='Integer')
# number of buses
num_buses = LpVariable("NumBuses", lowBound=0, upBound=4, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("EmployeeTransportationProblem", LpMinimize)

# Define the objective function
# minimize the total pollution produced
objective = 10 * num_cars + 30 * num_buses
problem += objective

# Define the constraints
# total employees transported
problem += 4 * num_cars + 20 * num_buses >= 300

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of cars:", num_cars.value())
print("The number of buses:", num_buses.value())
print("Total pollution produced:", objective.value())
print("## end solving")