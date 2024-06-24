from pulp import *

# Define the decision variables
# number of subsoil bags
num_subsoil_bags = LpVariable("NumSubsoilBags", lowBound=0, cat='Integer')
# number of topsoil bags
num_topsoil_bags = LpVariable("NumTopsoilBags", lowBound=10, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("GardenBedProblem", LpMinimize)

# Define the objective function
# minimize the total amount of water required to hydrate the garden bed
objective = 10 * num_subsoil_bags + 6 * num_topsoil_bags
problem += objective

# Define the constraints
# total number of bags available
problem += num_subsoil_bags + num_topsoil_bags <= 150
# at most 30% of all bags of soil can be topsoil
problem += num_topsoil_bags <= 0.3 * (num_subsoil_bags + num_topsoil_bags)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of subsoil bags:", num_subsoil_bags.value())
print("The number of topsoil bags:", num_topsoil_bags.value())
print("The total amount of water required:", objective.value())
print("## end solving")