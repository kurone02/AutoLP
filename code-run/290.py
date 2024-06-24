from pulp import *

# Define the decision variables
num_circular_tables = LpVariable("NumCircularTables", lowBound=0, cat='Integer')
num_rectangular_tables = LpVariable("NumRectangularTables", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("ScienceFairTables", LpMaximize)

# Define the objective function
problem += 8 * num_circular_tables + 12 * num_rectangular_tables

# Define the constraints
problem += 5 * num_circular_tables + 4 * num_rectangular_tables >= 500
problem += 4 * num_circular_tables + 4 * num_rectangular_tables >= 300
problem += 15 * num_circular_tables + 20 * num_rectangular_tables <= 1900

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of circular tables:", num_circular_tables.value())
print("The number of rectangular tables:", num_rectangular_tables.value())
print("The total number of catered guests:", value(problem.objective))
print("## end solving")