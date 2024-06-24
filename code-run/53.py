from pulp import *

# Define the decision variables
# number of milk chocolate pieces
num_milk_choco = LpVariable("NumMilkChoco", lowBound=0, cat='Integer')
# number of dark chocolate pieces
num_dark_choco = LpVariable("NumDarkChoco", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("BakerProblem", LpMinimize)

# Define the objective function
# minimize the total cost
objective = 0.5 * num_milk_choco + 0.75 * num_dark_choco
problem += objective

# Define the constraints
# total cacao
problem += 3 * num_milk_choco + 4 * num_dark_choco >= 120
# total sugar
problem += 2 * num_milk_choco + 1 * num_dark_choco >= 80
# milk chocolate pieces constraint
problem += num_milk_choco >= 0
# dark chocolate pieces constraint
problem += num_dark_choco >= 0

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of milk chocolate pieces:", num_milk_choco.value())
print("The number of dark chocolate pieces:", num_dark_choco.value())
print("The total cost:", objective.value())
print("## end solving")