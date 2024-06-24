from pulp import *

# Define the decision variables
num_rural_factories = LpVariable("NumRuralFactories", lowBound=0, cat='Integer')
num_urban_factories = LpVariable("NumUrbanFactories", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("CellPhoneFactoryProblem", LpMinimize)

# Define the objective function
objective = num_rural_factories + num_urban_factories
problem += objective

# Define the constraints
problem += 100 * num_rural_factories + 200 * num_urban_factories >= 3000
problem += 8 * num_rural_factories + 20 * num_urban_factories <= 260

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of rural factories:", num_rural_factories.value())
print("The number of urban factories:", num_urban_factories.value())
print("The total number of factories:", objective.value())
print("## end solving")