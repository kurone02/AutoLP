from pulp import *

# Define the variables
num_sling_chairs = LpVariable("NumSlingChairs", lowBound=0, cat='Integer')
num_adirondack_chairs = LpVariable("NumAdirondackChairs", lowBound=0, cat='Integer')
num_hammocks = LpVariable("NumHammocks", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("ChairProductionProblem", LpMaximize)
objective = 40 * num_sling_chairs + 100 * num_adirondack_chairs + 90 * num_hammocks
problem += objective

# Define the constraints
problem += 30 * num_sling_chairs + 2 * num_adirondack_chairs + 0.4 * num_hammocks <= 50
problem += 45 * num_sling_chairs + 3 * num_hammocks <= 50
problem += num_sling_chairs + num_adirondack_chairs + num_hammocks <= 50
problem += (30 * num_sling_chairs + 45 * num_sling_chairs + 0.4 * num_hammocks + 2 * num_adirondack_chairs + 3 * num_hammocks) * 4 <= 120

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of sling chairs to produce:", value(num_sling_chairs))
print("The number of Adirondack chairs to produce:", value(num_adirondack_chairs))
print("The number of hammocks to produce:", value(num_hammocks))
print("The maximum profit:", value(objective))
print("## end solving")