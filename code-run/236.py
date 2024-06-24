from pulp import *

# Define the decision variables
# number of milk chocolate bars
num_milk_chocolate = LpVariable("NumMilkChocolate", lowBound=0, cat='Integer')
# number of dark chocolate bars
num_dark_chocolate = LpVariable("NumDarkChocolate", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("ChocolateShopProblem", LpMinimize)

# Define the objective function
# minimize the total production time
objective = 15 * num_milk_chocolate + 12 * num_dark_chocolate
problem += objective

# Define the constraints
# total cocoa
problem += 4 * num_milk_chocolate + 6 * num_dark_chocolate <= 2000
# total milk
problem += 7 * num_milk_chocolate + 3 * num_dark_chocolate <= 1750
# at least 2 times as many milk chocolate bars
problem += num_milk_chocolate >= 2 * num_dark_chocolate

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of milk chocolate bars:", num_milk_chocolate.value())
print("The number of dark chocolate bars:", num_dark_chocolate.value())
print("Total production time:", objective.value())
print("## end solving")