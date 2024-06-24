from pulp import *

# Define the decision variables
# number of tables to produce
num_tables = LpVariable("NumTables", lowBound=0, cat='Integer')
# number of chairs to produce
num_chairs = LpVariable("NumChairs", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("LegoFurnitureProblem", LpMaximize)

# Define the objective function
# maximize the total revenue
objective = 35 * num_tables + 29 * num_chairs
problem += objective

# Define the constraints
# the number of chairs produced must be at least 4 times the number of tables
problem += num_chairs >= 4 * num_tables
# the amount of large wood required for tables and chairs must not exceed the available amount
problem += 3 * num_tables + 1 * num_chairs <= 300
problem += 2 * num_tables + 4 * num_chairs <= 500

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of tables to produce:", num_tables.value())
print("The number of chairs to produce:", num_chairs.value())
print("The total revenue generated:", round(objective.value()))
print("## end solving")