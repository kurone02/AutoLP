from pulp import *

# Define the decision variables
# number of miter saws
num_miter_saws = LpVariable("NumMiterSaws", lowBound=0, cat='Integer')
# number of circular saws
num_circular_saws = LpVariable("NumCircularSaws", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("WoodshopSawPurchaseProblem", LpMinimize)

# Define the objective function
# minimize the total number of saws needed
objective = num_miter_saws + num_circular_saws
problem += objective

# Define the constraints
# total number of planks of wood cut
problem += 50 * num_miter_saws + 70 * num_circular_saws >= 1500
# total amount of sawdust produced
problem += 60 * num_miter_saws + 100 * num_circular_saws <= 2000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of miter saws:", num_miter_saws.value())
print("The number of circular saws:", num_circular_saws.value())
print("## end solving")