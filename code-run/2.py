from pulp import *

# Define the decision variables
# number of bedside tables produced
num_bedside_tables = LpVariable("NumBedsideTables", lowBound=0, cat='Integer')
# number of bookcases produced
num_bookcases = LpVariable("NumBookcases", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("FurnitureFactoryProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 200 * num_bedside_tables + 500 * num_bookcases
problem += objective

# Define the constraints
# total crafting hours
problem += 2.5 * num_bedside_tables + 5 * num_bookcases <= 30
# total polishing hours
problem += 1.5 * num_bedside_tables + 3 * num_bookcases <= 20

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of bedside tables produced:", num_bedside_tables.value())
print("The number of bookcases produced:", num_bookcases.value())
print("The total profit:", objective.value())
print("## end solving")