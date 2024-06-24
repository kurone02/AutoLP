from pulp import *

# Define the decision variables
# number of acres of pineapples
num_pineapples = LpVariable("NumPineapples", lowBound=40, cat='Integer')
# number of acres of bananas
num_bananas = LpVariable("NumBananas", lowBound=60, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("FarmerProfitProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 200 * num_pineapples + 150 * num_bananas
problem += objective

# Define the constraints
# total acres available
problem += num_pineapples + num_bananas <= 200
# bananas should not be more than 4 times the amount of pineapples
problem += num_bananas <= 4 * num_pineapples
# minimum acre requirement for pineapples
problem += num_pineapples >= 40
# minimum acre requirement for bananas
problem += num_bananas >= 60

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of acres of pineapples:", num_pineapples.value())
print("The number of acres of bananas:", num_bananas.value())
print("The maximum profit:", objective.value())
print("## end solving")