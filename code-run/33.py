from pulp import *

# Define the decision variables
# number of first-class tickets
num_first_class = LpVariable("NumFirstClass", lowBound=20, cat='Integer')
# number of economy-class tickets
num_economy = LpVariable("NumEconomy", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("FlightTicketProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 150 * num_first_class + 350 * num_economy
problem += objective

# Define the constraints
# total number of tickets
problem += num_first_class + num_economy <= 150
# people prefer to save money and travel by economy-class than first-class
problem += num_economy >= 3 * num_first_class

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of first-class tickets:", num_first_class.value())
print("The number of economy-class tickets:", num_economy.value())
print("The maximum profit:", objective.value())
print("## end solving")