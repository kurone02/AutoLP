from pulp import *

# Define the decision variables
# number of automatic electric jacks
num_automatic_jacks = LpVariable("NumAutomaticJacks", lowBound=0, cat='Integer')
# number of gas jacks
num_gas_jacks = LpVariable("NumGasJacks", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("AutoBodyShopProblem", LpMaximize)

# Define the objective function
# maximize the total cars processed
objective = 5 * num_automatic_jacks + 4 * num_gas_jacks
problem += objective

# Define the constraints
# number of automatic electric jacks constraint
problem += num_automatic_jacks <= 15
# total units of electricity constraint
problem += 6 * num_automatic_jacks <= 50
# total units of gas constraint
problem += 7 * num_gas_jacks <= 80

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of automatic jacks:", num_automatic_jacks.value())
print("The number of gas jacks:", num_gas_jacks.value())
print("The number of cars processed per hour:", objective.value())
print("## end solving")