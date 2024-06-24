from pulp import *

# Define the decision variables
# number of medium sized carts
num_medium_sized_carts = LpVariable("NumMediumSizedCarts", lowBound=5, cat='Integer')
# number of large sized carts
num_large_sized_carts = LpVariable("NumLargeSizedCarts", lowBound=5, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("FactoryRiceTransportation", LpMaximize)

# Define the objective function
# maximize the total amount of rice that can be transported
objective = 30 * num_medium_sized_carts + 70 * num_large_sized_carts
problem += objective

# Define the constraints
# total number of horses available
problem += 2 * num_medium_sized_carts + 4 * num_large_sized_carts <= 60
# the number of medium sized carts must be three times the number of large sized carts
problem += num_medium_sized_carts == 3 * num_large_sized_carts
# there must be at least 5 medium sized carts
problem += num_medium_sized_carts >= 5
# there must be at least 5 large sized carts
problem += num_large_sized_carts >= 5

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of medium sized carts:", num_medium_sized_carts.value())
print("The number of large sized carts:", num_large_sized_carts.value())
print("The amount of rice transported:", objective.value())
print("## end solving")