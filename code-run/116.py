from pulp import *

# Define the variables
num_scooters = LpVariable("NumScooters", lowBound=0, cat='Integer')
num_bikes = LpVariable("NumBikes", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("CompanyProfitMaximization", LpMaximize)
objective = 200 * num_scooters + 300 * num_bikes
problem += objective

# Define the constraints
problem += 2 * num_scooters + 4 * num_bikes <= 5000
problem += 3 * num_scooters + 5 * num_bikes <= 6000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of scooters:", value(num_scooters))
print("The number of bikes:", value(num_bikes))
print("Total profit:", value(objective))
print("## end solving")