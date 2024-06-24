from pulp import *

# Define the decision variables
# number of mechanical keyboards
num_mechanical = LpVariable("NumMechanical", lowBound=0, cat='Integer')
# number of standard keyboards
num_standard = LpVariable("NumStandard", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("KeyboardProblem", LpMaximize)

# Define the objective function
# maximize the total number of keyboards
problem += num_mechanical + num_standard

# Define the constraints
# total plastic
problem += 5 * num_mechanical + 2 * num_standard <= 1000
# total solder
problem += num_mechanical + 2 * num_standard <= 800
# standard keyboards constraint
problem += num_standard >= 30
# mechanical keyboards constraint
problem += num_mechanical >= 5 * num_standard

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of mechanical keyboards:", num_mechanical.value())
print("The number of standard keyboards:", num_standard.value())
print("The total number of keyboards:", (num_mechanical + num_standard).value())
print("## end solving")