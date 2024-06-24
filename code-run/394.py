from pulp import *

# Define the decision variables
num_simple_canoes = LpVariable("NumSimpleCanoes", lowBound=0, cat='Integer')
num_luxury_canoes = LpVariable("NumLuxuryCanoes", lowBound=0, cat='Integer')

# Define the question as a maximum problem
problem = LpProblem("CanoeProductionProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 7 * num_simple_canoes + 10 * num_luxury_canoes
problem += objective

# Define the constraints
# total number of canoes
problem  += num_luxury_canoes + num_simple_canoes >= 342.857142857143 # problem += num_simple_canoes + num_luxury_canoes >= 1/3 * 120 * 30 / 3.5
problem  += num_luxury_canoes + num_simple_canoes <= 685.714285714286 # problem += num_simple_canoes + num_luxury_canoes <= 2/3 * 120 * 30 / 3.5

# simple canoes
problem  += num_simple_canoes <= 400.0 # problem += num_simple_canoes <= 1/2 * 120 * 30 / 4.5

# luxury canoes
problem  += num_luxury_canoes <= 60 # problem += num_luxury_canoes <= 1/2 * 20 * 30 / 5
problem  += num_luxury_canoes <= 600 # problem += num_luxury_canoes <= 20 * 30 / 1
problem  += num_luxury_canoes <= 450 # problem += num_luxury_canoes <= 1/2 * 120 * 30 / 4

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of simple canoes to produce:", num_simple_canoes.value())
print("The number of luxury canoes to produce:", num_luxury_canoes.value())
print("The maximum overall net profit:", objective.value())
print("## end solving")