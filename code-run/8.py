from pulp import *

# Define the decision variables
# number of mango-lovers packages
num_mango_lovers_packages = LpVariable("NumMangoLoversPackages", lowBound=0, cat='Integer')
# number of regular packages
num_regular_packages = LpVariable("NumRegularPackages", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("FruitStoreProfitMaximization", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 5 * num_mango_lovers_packages + 6.5 * num_regular_packages
problem += objective

# Define the constraints
# total lemons used
problem += 4 * num_mango_lovers_packages + 3 * num_regular_packages <= 30
# total mangos used
problem += 8 * num_mango_lovers_packages + 5 * num_regular_packages <= 40
# total pears used
problem += 10 * num_regular_packages <= 50

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of mango-lovers packages:", num_mango_lovers_packages.value())
print("The number of regular packages:", num_regular_packages.value())
print("Net profit:", objective.value())
print("## end solving")