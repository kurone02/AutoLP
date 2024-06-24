from pulp import *

# Define the decision variables
# number of four-color litho to produce
num_four_color = LpVariable("NumFourColor", lowBound=2, cat='Integer')
# number of two-color litho to produce
num_two_color = LpVariable("NumTwoColor", lowBound=2, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("DMCProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 24000 * num_four_color + 10000 * num_two_color
problem += objective

# Define the constraints
# steel roller constraint
problem += 16 * num_four_color + 8 * num_two_color <= 100
# gear cutting constraint
problem += 30 * num_four_color + 12 * num_two_color <= 160
# roller polishing constraint
problem += 8 * num_four_color + 3 * num_two_color <= 40

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of four-color litho to produce:", num_four_color.value())
print("The number of two-color litho to produce:", num_two_color.value())
print("The maximum profit:", objective.value())
print("## end solving")