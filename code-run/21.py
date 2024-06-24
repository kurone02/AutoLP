from pulp import *

# Define the variables
num_heated_seats = LpVariable("NumHeatedSeats", lowBound=15, cat='Integer')
num_regular_seats = LpVariable("NumRegularSeats", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("TrainSeatSalesProblem", LpMaximize)
objective = 20 * num_heated_seats + 15 * num_regular_seats
problem += objective

# Define the constraints
problem += num_heated_seats + num_regular_seats <= 100
problem += num_regular_seats >= 3 * num_heated_seats

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of heated seats sold:", value(num_heated_seats))
print("The number of regular seats sold:", value(num_regular_seats))
print("Total profit:", value(objective))
print("## end solving")