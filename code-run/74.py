from pulp import *

# Define the decision variables
# number of flight jackets
num_flight_jackets = LpVariable("NumFlightJackets", lowBound=0, cat='Integer')
# number of denim jackets
num_denim_jackets = LpVariable("NumDenimJackets", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("ClothingCompanyProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 70 * num_flight_jackets + 100 * num_denim_jackets
problem += objective

# Define the constraints
# flight jacket constraint
problem += num_flight_jackets <= 10
# denim jacket constraint
problem += num_denim_jackets <= 25
# total jacket constraint
problem += num_flight_jackets + num_denim_jackets <= 30

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of flight jackets to produce:", num_flight_jackets.value())
print("The number of denim jackets to produce:", num_denim_jackets.value())
print("The maximum profit:", objective.value())
print("## end solving")