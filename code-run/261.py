from pulp import *

# Define the decision variables
# number of black milk tea bottles
num_black = LpVariable("NumBlack", lowBound=0, cat='Integer')
# number of matcha milk tea bottles
num_matcha = LpVariable("NumMatcha", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("MilkTeaShopProfitMaximization", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 7.5 * num_black + 5 * num_matcha
problem += objective

# Define the constraints
# total amount of milk
problem += 600 * num_black + 525 * num_matcha <= 30000
# total amount of honey
problem += 10 * num_black + 5 * num_matcha <= 500

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of black milk tea bottles:", num_black.value())
print("The number of matcha milk tea bottles:", num_matcha.value())
print("The maximum profit:", objective.value())
print("## end solving")