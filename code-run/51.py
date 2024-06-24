from pulp import *

# Define the decision variables
# number of heated seats sold
num_heated_seats = LpVariable("NumHeatedSeats", lowBound=50, cat='Integer')
# number of regular seats sold
num_regular_seats = LpVariable("NumRegularSeats", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("HockeyArenaProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 30 * num_heated_seats + 20 * num_regular_seats
problem += objective

# Define the constraints
# total number of seats sold
problem += num_heated_seats + num_regular_seats <= 300
# at least 3 times as many people prefer to sit in regular seats
problem += num_regular_seats >= 3 * (num_heated_seats + num_regular_seats)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of heated seats sold:", num_heated_seats.value())
print("The number of regular seats sold:", num_regular_seats.value())
print("The maximum profit:", objective.value())
print("## end solving")