from pulp import *

# Define the variables
num_sedans = LpVariable("NumSedans", lowBound=0, cat='Integer')
num_buses = LpVariable("NumBuses", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("TourismCompanyProblem", LpMinimize)

# Define the objective function
# minimize the total number of vehicles needed
objective = num_sedans + num_buses
problem += objective

# Define the constraints
problem += 10 * num_sedans + 40 * num_buses <= 800
problem += 50 * num_sedans + 250 * num_buses >= 4600

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of sedans to purchase:", num_sedans.value())
print("The number of buses to purchase:", num_buses.value())
print("The total number of vehicles:", objective.value())
print("## end solving")