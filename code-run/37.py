from pulp import *

# Define the decision variables
num_dining_tables = LpVariable("NumDiningTables", lowBound=0, cat='Integer')
num_coffee_tables = LpVariable("NumCoffeeTables", lowBound=0, cat='Integer') 

# Define the problem
problem = LpProblem("FurnitureProblem", LpMaximize)

# Define the objective function
objective = 200 * num_dining_tables + 100 * num_coffee_tables
problem += objective

# Define the constraints
problem += 250 * num_dining_tables + 150 * num_coffee_tables <= 20000
problem += num_dining_tables + num_coffee_tables <= 200

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of dining tables:", num_dining_tables.value())
print("The number of coffee tables:", num_coffee_tables.value())
print("The total profit:", objective.value())
print("## end solving")