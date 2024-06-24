from pulp import *

# Define the decision variables
# number of sling chairs to produce
num_sling_chairs = LpVariable("NumSlingChairs", lowBound=0, cat='Integer')
# number of Adirondack chairs to produce
num_adirondack_chairs = LpVariable("NumAdirondackChairs", lowBound=0, cat='Integer')
# number of hammocks to produce
num_hammocks = LpVariable("NumHammocks", lowBound=0, cat='Integer')

# Define the question as a minimum or maximum problem
problem = LpProblem("ChairProductionProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 40 * num_sling_chairs + 100 * num_adirondack_chairs + 90 * num_hammocks
problem += objective

# Define the constraints
# total time spent on cutting
problem += 0.5 * num_sling_chairs + 2 * num_adirondack_chairs + 0.4 * num_hammocks <= 50
# total time spent on assembling
problem += 0.75 * num_sling_chairs + 2 * num_adirondack_chairs + 3 * num_hammocks <= 50
# total time spent on finishing
problem += num_sling_chairs + num_adirondack_chairs + num_hammocks <= 120

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of sling chairs to produce:", num_sling_chairs.value())
print("The number of Adirondack chairs to produce:", num_adirondack_chairs.value())
print("The number of hammocks to produce:", num_hammocks.value())
print("The maximum profit:", objective.value())
print("## end solving")