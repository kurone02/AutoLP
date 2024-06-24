from pulp import *

# Define the decision variables
# number of bags from Bag A
num_bags_A = LpVariable("NumBagsA", lowBound=0, cat='Integer')
# number of bags from Bag B
num_bags_B = LpVariable("NumBagsB", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("PetStoreProblem", LpMinimize)

# Define the objective function
# minimize the total cost of the mixture
objective = 3.5 * num_bags_A + 2.5 * num_bags_B
problem += objective

# Define the constraints
# The mixture must contain at least 30 units of protein
problem += 3 * num_bags_A + 4 * num_bags_B >= 30
# The mixture must contain at least 35 units of calcium
problem += 4 * num_bags_A + 2 * num_bags_B >= 35

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of bags from Bag A:", num_bags_A.value())
print("The number of bags from Bag B:", num_bags_B.value())
print("The cost of the mixture:", objective.value())
print("## end solving")