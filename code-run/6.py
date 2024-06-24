from pulp import *

# Define the decision variables
# number of acres of lavender
num_acres_lavender = LpVariable("NumAcresLavender", lowBound=5, cat='Integer')
# number of acres of tulips
num_acres_tulips = LpVariable("NumAcresTulips", lowBound=8, cat='Integer') 

# Define the problem
problem = LpProblem("GardenerProblem", LpMaximize)
objective = 250 * num_acres_lavender + 200 * num_acres_tulips
problem += objective

# Define the constraints
problem += num_acres_lavender + num_acres_tulips <= 50
problem += num_acres_lavender >= 5
problem += num_acres_tulips >= 8
problem += num_acres_lavender <= 2 * num_acres_tulips

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of acres of lavender grown:", value(num_acres_lavender))
print("The number of acres of tulips grown:", value(num_acres_tulips))
print("Total profit:", value(objective))
print("## end solving")