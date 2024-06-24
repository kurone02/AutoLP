from pulp import *

# Define the decision variables
# number of large ships
num_large_ships = LpVariable("NumLargeShips", lowBound=0, cat='Integer')
# number of small ships
num_small_ships = LpVariable("NumSmallShips", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("ShippingCompanyProblem", LpMinimize)

# Define the objective function
# minimize the total number of ships
objective = num_large_ships + num_small_ships
problem += objective

# Define the constraints
# total number of containers
problem += 500 * num_large_ships + 200 * num_small_ships >= 3000
# number of large ships cannot exceed the number of small ships
problem += num_large_ships <= num_small_ships

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of large ships:", num_large_ships.value())
print("The number of small ships:", num_small_ships.value())
print("The minimum number of ships needed:", objective.value())
print("## end solving")