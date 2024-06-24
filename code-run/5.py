from pulp import *

# Define the decision variables
# number of low quality face wash
num_low = LpVariable("NumLow", lowBound=0, cat='Integer')
# number of medium quality face wash
num_medium = LpVariable("NumMedium", lowBound=0, cat='Integer') 
# number of high quality face wash
num_high = LpVariable("NumHigh", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("CosmeticsProfitProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 3 * num_low + 7 * num_medium + 9 * num_high
problem += objective

# Define the constraints
# total rare ingredients
problem += 1 * num_low + 3 * num_medium + 4 * num_high <= 100
# total water
problem += 4 * num_low + 2 * num_medium + 1 * num_high <= 200

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of low quality face wash:", num_low.value())
print("The number of medium quality face wash:", num_medium.value())
print("The number of high quality face wash:", num_high.value())
print("The total profit:", objective.value())
print("## end solving")