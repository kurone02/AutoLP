from pulp import *

# Define the decision variables
num_jars = LpVariable("NumJars", lowBound=0, cat='Integer')
num_plates = LpVariable("NumPlates", lowBound=0, cat='Integer') 

# Define the problem
problem = LpProblem("FactoryProblem", LpMaximize)

# Define the objective function
problem += 2 * num_jars + 2.5 * num_plates

# Define the constraints
problem += 15 * num_jars + 12 * num_plates <= 620
problem += 3 * num_jars + 4 * num_plates <= 120

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of glass jars to package:", num_jars.value())
print("The number of plates to package:", num_plates.value())
print("The maximum profit:", problem.objective.value())
print("## end solving")