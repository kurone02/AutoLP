from pulp import *

# Define the decision variables
# number of acres of pumpkins to plant
num_pumpkins = LpVariable("AcresPumpkins", lowBound=7, cat='Integer')
# number of acres of carrots to plant
num_carrots = LpVariable("AcresCarrots", lowBound=12, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("GabrielFarmProblem", LpMaximize)

# Define the objective function
# maximize the total profit from growing pumpkins and carrots
objective = 2.5 * num_pumpkins + 3.4 * num_carrots
problem += objective

# Define the constraints
# total acres to plant
problem += num_pumpkins + num_carrots <= 100
# preferred ratio of carrots to pumpkins
problem += num_carrots <= 3 * num_pumpkins

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of acres of pumpkins to plant:", num_pumpkins.value())
print("The number of acres of carrots to plant:", num_carrots.value())
print("The maximum profit:", objective.value())
print("## end solving")