from pulp import *

# Define the decision variables
# number of plush toys
num_plush_toys = LpVariable("NumPlushToys", lowBound=90, upBound=190, cat='Integer')
# number of dolls
num_dolls = LpVariable("NumDolls", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("ToyStoreProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 4 * num_plush_toys + 2 * num_dolls
problem += objective

# Define the constraints
# total cost
problem += 3 * num_plush_toys + 2 * num_dolls <= 700
# dolls sold constraint
problem += num_dolls <= 2 * num_plush_toys

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of plush toys:", num_plush_toys.value())
print("The number of dolls:", num_dolls.value())
print("The profit made:", objective.value())
print("## end solving")