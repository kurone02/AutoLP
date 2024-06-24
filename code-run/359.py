from pulp import *

# Define the decision variables
# number of wine units
num_wine = LpVariable("NumWine", lowBound=0, cat='Integer')
# number of kombucha units
num_kombucha = LpVariable("NumKombucha", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("BreweryProblem", LpMinimize)

# Define the objective function
# minimize the total units of fruit required
objective = 3 * num_wine + 5 * num_kombucha
problem += objective

# Define the constraints
# the number of wine units must be larger than the number of kombucha units
problem += num_wine >= num_kombucha
# the company has available 7000 units of water and 9000 units of tea
problem += 8 * num_wine + 7 * num_kombucha <= 7000
# at least 20% of their products made must be kombucha
problem += num_kombucha >= 0.2 * (num_wine + num_kombucha)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of wine units:", num_wine.value())
print("The number of kombucha units:", num_kombucha.value())
print("The total units of fruit required:", objective.value())
print("## end solving")