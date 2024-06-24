from pulp import *

# Define the decision variables
# number of regular brand bags
num_regular = LpVariable("NumRegular", lowBound=0, cat='Integer')
# number of premium brand bags
num_premium = LpVariable("NumPremium", lowBound=0, cat='Integer') 

# Define the problem
problem = LpProblem("LucyDogFoodProblem", LpMinimize)
objective = 20 * num_regular + 35 * num_premium
problem += objective

# Define the constraints
problem += 4 * num_regular + 12 * num_premium >= 15
problem += 7 * num_regular + 10 * num_premium >= 20
problem += 10 * num_regular + 16 * num_premium >= 20
problem += num_regular + num_premium >= 1

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of regular brand bags:", num_regular.value())
print("The number of premium brand bags:", num_premium.value())
print("The total cost:", objective.value())
print("## end solving")