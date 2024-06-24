from pulp import *

# Define the decision variables
num_escalators = LpVariable("NumEscalators", lowBound=0, cat='Integer')
num_elevators = LpVariable("NumElevators", lowBound=2, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("AirportTransportation", LpMinimize)

# Define the objective function
# minimize the total units of space taken
objective = num_escalators * 5 + num_elevators * 2
problem += objective

# Define the constraints
# total capacity of the airport
problem += num_escalators * 20 + num_elevators * 8 >= 400
# at least three times more escalators than elevators
problem += num_escalators >= 3 * num_elevators

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of escalators:", num_escalators.value())
print("The number of elevators:", num_elevators.value())
print("The total units of space taken:", objective.value())
print("## end solving")