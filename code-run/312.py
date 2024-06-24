from pulp import *

# Define the decision variables
# number of large bags
num_large_bags = LpVariable("NumLargeBags", lowBound=0, cat='Integer')
# number of tiny bags
num_tiny_bags = LpVariable("NumTinyBags", lowBound=20, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("GrainTransportationProblem", LpMaximize)

# Define the objective function
# maximize the total weight of grain transported
objective = 25 * num_large_bags + 6 * num_tiny_bags
problem += objective

# Define the constraints
# energy constraint
problem += 4 * num_large_bags + 1.5 * num_tiny_bags <= 110
# popularity constraint
problem += num_large_bags == 2 * num_tiny_bags

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of large bags:", num_large_bags.value())
print("The number of tiny bags:", num_tiny_bags.value())
print("The total weight of grain transported:", objective.value())
print("## end solving")