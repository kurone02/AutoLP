from pulp import *

# Define the decision variables
# number of black milk tea to make
num_black_tea = LpVariable("NumBlackTea", lowBound=0, cat='Integer')
# number of green milk tea to make
num_green_tea = LpVariable("NumGreenTea", lowBound=10, cat='Integer') 

# Define the question as a maximum or minimum problem
problem = LpProblem("MilkTeaShopProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 2.5 * num_black_tea + 7 * num_green_tea
problem += objective

# Define the constraints
# total amount of milk available
problem += 300 * num_black_tea + 200 * num_green_tea <= 50000
# number of black milk tea constraint
problem += num_black_tea >= 3 * num_green_tea
# number of green milk tea constraint
problem += num_green_tea >= 10

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of bottles of black milk tea:", num_black_tea.value())
print("The number of bottles of green milk tea:", num_green_tea.value())
print("Total profit:", objective.value())
print("## end solving")