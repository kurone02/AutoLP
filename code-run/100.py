from pulp import *

# Define the decision variables
# number of large art pieces
num_large_art = LpVariable("NumLargeArt", lowBound=5, cat='Integer')
# number of small art pieces
num_small_art = LpVariable("NumSmallArt", lowBound=5, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("ArtStoreProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 30 * num_large_art + 15 * num_small_art
problem += objective

# Define the constraints
# total paint
problem += 4 * num_large_art + 2 * num_small_art <= 100
# total glitter
problem += 3 * num_large_art + 1 * num_small_art <= 50
# total glue
problem += 5 * num_large_art + 2 * num_small_art <= 70
# minimum number of large art pieces
problem += num_large_art >= 5
# minimum number of small art pieces
problem += num_small_art >= 5

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of large art pieces:", num_large_art.value())
print("The number of small art pieces:", num_small_art.value())
print("The total profit:", objective.value())
print("## end solving")