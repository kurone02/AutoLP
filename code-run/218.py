from pulp import *

# Define the decision variables
# number of small bouquets
num_small_bouquets = LpVariable("NumSmallBouquets", lowBound=0, cat='Integer')
# number of large bouquets
num_large_bouquets = LpVariable("NumLargeBouquets", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("FloristProblem", LpMaximize)

# Define the objective function
# maximize the total number of flowers
objective = 5 * num_small_bouquets + 10 * num_large_bouquets
problem += objective

# Define the constraints
# total number of bouquets
problem += num_small_bouquets + num_large_bouquets <= 70
# total number of small bouquets
problem += num_small_bouquets <= 80
# total number of large bouquets
problem += num_large_bouquets <= 50
# minimum number of large bouquets
problem += num_large_bouquets >= 20
# minimum number of small bouquets
problem += num_small_bouquets >= 2 * num_large_bouquets

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of small bouquets:", num_small_bouquets.value())
print("The number of large bouquets:", num_large_bouquets.value())
print("The total number of flowers transported:", objective.value())
print("## end solving")