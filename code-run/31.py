from pulp import *

# Define the decision variables
# number of race cars
num_race_cars = LpVariable("NumRaceCars", lowBound=0, cat='Integer')
# number of regular cars
num_regular_cars = LpVariable("NumRegularCars", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("CarCompanyProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 20000 * num_race_cars + 10000 * num_regular_cars
problem += objective

# Define the constraints
# race car team constraint
problem += num_race_cars <= 3
# regular car team constraint
problem += num_regular_cars <= 5
# safety check constraint
problem += num_race_cars + num_regular_cars <= 6

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of race cars produced per day:", num_race_cars.value())
print("The number of regular cars produced per day:", num_regular_cars.value())
print("The total profit per day:", objective.value())
print("## end solving")