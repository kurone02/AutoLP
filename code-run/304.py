from pulp import *

# Define the decision variables
# number of blueberry packs
num_blueberries = LpVariable("NumBlueberries", lowBound=0, cat='Integer')
# number of strawberry packs
num_strawberries = LpVariable("NumStrawberries", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("DieticianProblem", LpMinimize)

# Define the objective function
# minimize the total sugar intake
objective = 5 * num_blueberries + 7 * num_strawberries
problem += objective

# Define the constraints
# minimum anti-oxidants
problem += 3 * num_blueberries + 1 * num_strawberries >= 90
# minimum minerals
problem += 5 * num_blueberries + 7 * num_strawberries >= 100
# strawberries are not in season
problem += num_strawberries >= 3 * num_blueberries

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of blueberry packs:", num_blueberries.value())
print("The number of strawberry packs:", num_strawberries.value())
print("The total sugar intake from packs:", objective.value())
print("## end solving")