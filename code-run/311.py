from pulp import *

# Define the decision variables
num_bike_shifts = LpVariable("BikeShifts", lowBound=0, cat='Integer')
num_scooter_shifts = LpVariable("ScooterShifts", lowBound=5, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("FoodDeliveryProblem", LpMaximize)

# Define the objective function
objective = 50 * num_bike_shifts + 43 * num_scooter_shifts
problem += objective

# Define the constraints
problem += num_bike_shifts + num_scooter_shifts <= 40
problem += 5 * num_bike_shifts + 6 * num_scooter_shifts <= 230
problem += 10 * num_bike_shifts + 7 * num_scooter_shifts >= 320

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of bike shifts:", num_bike_shifts.value())
print("The number of scooter shifts:", num_scooter_shifts.value())
print("The total tips received:", objective.value())
print("## end solving")