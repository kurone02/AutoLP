from pulp import *

# Define the variables
num_bikes = LpVariable("NumBikes", lowBound=0, cat='Integer')
num_scooters = LpVariable("NumScooters", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("MealServiceProblem", LpMaximize)
objective = 8 * num_bikes + 5 * num_scooters
problem += objective

# Define the constraints
problem += 3 * num_bikes + 2 * num_scooters <= 200
problem += num_bikes <= 0.3 * (num_bikes + num_scooters)
problem += num_scooters >= 20

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of bikes:", value(num_bikes))
print("The number of scooters:", value(num_scooters))
print("The number of meals delivered:", value(objective))
print("## end solving")