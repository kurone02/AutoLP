from pulp import *

# Define the decision variables
# number of acres for small oil wells
num_acres_small = LpVariable("AcresSmall", lowBound=0, cat='Integer')
# number of acres for large oil wells
num_acres_large = LpVariable("AcresLarge", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("OilAndGasProblem", LpMaximize)

# Define the objective function
# maximize the total production of oil
objective = 2 * num_acres_small + 5 * num_acres_large
problem += objective

# Define the constraints
# total available drill bits
problem += 5 * num_acres_small + 10 * num_acres_large <= 2500
# total pollution produced
problem += 10 * num_acres_small + 20 * num_acres_large <= 4500
# total acres of land
problem += num_acres_small + num_acres_large <= 300

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of acres for small oil wells:", num_acres_small.value())
print("The number of acres for large oil wells:", num_acres_large.value())
print("The total production of oil:", objective.value())
print("## end solving")