from pulp import *

# Define the decision variables
# number of batches of bagels
num_bagels = LpVariable("NumBagels", lowBound=0, cat='Integer')
# number of batches of croissants
num_croissants = LpVariable("NumCroissants", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("BakeryProfitMaximization", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 20 * num_bagels + 40 * num_croissants
problem += objective

# Define the constraints
# total oven time
problem += 2 * num_bagels + 1 * num_croissants <= 70
# total pastry chef time
problem += 0.25 * num_bagels + 2 * num_croissants <= 32

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of batches of bagels:", num_bagels.value())
print("The number of batches of croissants:", num_croissants.value())
print("The maximum profit is:", objective.value())
print("## end solving")