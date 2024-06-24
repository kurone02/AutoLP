from pulp import *

# Define the decision variables
# number of small buses
num_small_buses = LpVariable("NumSmallBuses", lowBound=0, cat='Integer')
# number of large buses
num_large_buses = LpVariable("NumLargeBuses", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("SchoolBusHireProblem", LpMinimize)

# Define the objective function
# minimize the total number of buses
objective = num_small_buses + num_large_buses
problem += objective

# Define the constraints
# minimum student transport constraint
problem += 20 * num_small_buses + 50 * num_large_buses >= 500
# maximum large buses constraint
problem += num_large_buses <= 0.2 * (num_small_buses + num_large_buses)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of small buses:", num_small_buses.value())
print("The number of large buses:", num_large_buses.value())
print("The total number of buses:", objective.value())
print("## end solving")