from pulp import *

# Define the decision variables
num_retail_stores = LpVariable("NumRetailStores", lowBound=0, cat='Integer')
num_factory_outlets = LpVariable("NumFactoryOutlets", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("ClothingDistribution", LpMinimize)
objective = num_retail_stores + num_factory_outlets
problem += objective

# Define the constraints
problem += 200 * num_retail_stores + 80 * num_factory_outlets >= 1200
problem += 6 * num_retail_stores + 4 * num_factory_outlets <= 50

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of retail stores:", num_retail_stores.value())
print("The number of factory outlets:", num_factory_outlets.value())
print("The total number of stores:", num_retail_stores.value() + num_factory_outlets.value())
print("## end solving")