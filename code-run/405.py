from pulp import *

# Define the decision variables
num_tables = LpVariable("NumTables", lowBound=0, cat='Integer')
num_chairs = LpVariable("NumChairs", lowBound=0, cat='Integer') 

# Define the problem
problem = LpProblem("LegoFurnitureProblem", LpMaximize)

# Define the objective function
objective = 35 * num_tables + 29 * num_chairs
problem += objective

# Define the constraints
problem += 3 * num_tables + 2 * num_chairs <= 300
problem += num_chairs <= 500 * 4
problem += num_chairs == 4 * num_tables

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of tables to produce:", num_tables.value())
print("The number of chairs to produce:", num_chairs.value())
print("The total revenue generated:", round(objective.value()))
print("## end solving")