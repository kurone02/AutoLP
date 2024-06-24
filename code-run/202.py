from pulp import *

# Define the variables
num_chlorine = LpVariable("NumChlorine", lowBound=100, cat='Integer')
num_water_softener = LpVariable("NumWaterSoftener", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("PoolProblem", LpMinimize)
objective = num_chlorine + num_water_softener
problem += objective

# Define the constraints
problem += num_chlorine + num_water_softener <= 500
problem += num_chlorine >= 100
problem += num_chlorine <= 0.5 * num_water_softener

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of units of chlorine:", value(num_chlorine))
print("The number of units of water softener:", value(num_water_softener))
print("The total time for the pool to be ready:", value(objective))
print("## end solving")