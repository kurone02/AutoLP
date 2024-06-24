from pulp import *

# Define the decision variables
# number of long cables
num_long_cables = LpVariable("NumLongCables", lowBound=10, cat='Integer')
# number of short cables
num_short_cables = LpVariable("NumShortCables", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("GoldMiningProblem", LpMaximize)

# Define the objective function
# maximize the total profit from selling cables
objective = 12 * num_long_cables + 5 * num_short_cables
problem += objective

# Define the constraints
# gold constraint
problem += 10 * num_long_cables + 7 * num_short_cables <= 1000
# compact size constraint
problem += num_short_cables >= 5 * num_long_cables
# minimum long cable constraint
problem += num_long_cables >= 10

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of long cables:", num_long_cables.value())
print("The number of short cables:", num_short_cables.value())
print("The maximum profit:", objective.value())
print("## end solving")