from pulp import *

# Define the decision variables
# number of small bottles
num_small_bottles = LpVariable("NumSmallBottles", lowBound=0, cat='Integer')
# number of large bottles
num_large_bottles = LpVariable("NumLargeBottles", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("BeeFarmerProblem", LpMaximize)

# Define the objective function
# maximize the total amount of honey transported
objective = 5 * num_small_bottles + 20 * num_large_bottles
problem += objective

# Define the constraints
# small bottles constraint
problem += num_small_bottles <= 300
# large bottles constraint
problem += num_large_bottles <= 100
# small bottles vs large bottles constraint
problem += num_small_bottles >= 2 * num_large_bottles
# total bottles constraint
problem += num_small_bottles + num_large_bottles <= 200
# minimum large bottles constraint
problem += num_large_bottles >= 50

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of small bottles:", num_small_bottles.value())
print("The number of large bottles:", num_large_bottles.value())
print("The amount of honey transported:", objective.value())
print("## end solving")