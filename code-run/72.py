from pulp import *

# Define the decision variables
# number of small cabinets
num_small_cabinets = LpVariable("NumSmallCabinets", lowBound=0, cat='Integer')
# number of large cabinets
num_large_cabinets = LpVariable("NumLargeCabinets", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("CabinetProblem", LpMaximize)

# Define the objective function
# maximize the total number of seasonings and spices
objective = 30 * num_small_cabinets + 40 * num_large_cabinets
problem += objective

# Define the constraints
# total space
problem += 4 * num_small_cabinets + 8 * num_large_cabinets <= 200
# total budget
problem += 70 * num_small_cabinets + 120 * num_large_cabinets <= 1400

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of small cabinets:", num_small_cabinets.value())
print("The number of large cabinets:", num_large_cabinets.value())
print("The number of seasonings and spices stored:", objective.value())
print("## end solving")