from pulp import *

# Define the decision variables
# number of mango bubble teas
num_mango = LpVariable("NumMango", lowBound=0, cat='Integer')
# number of lychee bubble teas
num_lychee = LpVariable("NumLychee", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("BubbleTeaShopProblem", LpMinimize)

# Define the objective function
# minimize the total amount of tea needed
objective = 8 * num_mango + 6 * num_lychee
problem += objective

# Define the constraints
# total amount of mango juice
problem += 4 * num_mango <= 2000
# total amount of lychee juice
problem += 6 * num_lychee <= 3000
# at least 40% of the bubble teas made must be lychee flavored
problem += num_lychee >= 0.4 * (num_mango + num_lychee)
# mango bubble tea sells better
problem += num_mango >= num_lychee

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of mango bubble tea:", num_mango.value())
print("The number of lychee bubble tea:", num_lychee.value())
print("The total amount of tea needed:", objective.value())
print("## end solving")