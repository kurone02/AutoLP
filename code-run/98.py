from pulp import *

# Define the decision variables
num_regular_glass = LpVariable("NumRegularGlass", lowBound=0, cat='Integer')
num_tempered_glass = LpVariable("NumTemperedGlass", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("GlassFactoryProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 8 * num_regular_glass + 10 * num_tempered_glass
problem += objective

# Define the constraints
# time on the heating and cooling machine for regular glass
problem += 3 * num_regular_glass + 5 * num_tempered_glass <= 300
# time on the heating and cooling machine for tempered glass
problem += 5 * num_regular_glass + 8 * num_tempered_glass <= 300
# both panes need to be made
problem += num_regular_glass + num_tempered_glass >= 0

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of regular glass panes:", num_regular_glass.value())
print("The number of tempered glass panes:", num_tempered_glass.value())
print("The maximum profit:", objective.value())
print("## end solving")