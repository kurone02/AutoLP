from pulp import *

# Define the decision variables
# number of simple canoes
num_simple_canoes = LpVariable("NumSimpleCanoes", lowBound=0, cat='Integer')
# number of luxury canoes
num_luxury_canoes = LpVariable("NumLuxuryCanoes", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("CanoeManufacturingProblem", LpMaximize)

# Define the objective function
# maximize the total net profit
objective = 7 * num_simple_canoes + 10 * num_luxury_canoes
problem += objective

# Define the constraints
# total hours required for simple canoes
problem += 4.5 * num_simple_canoes + 5 * num_luxury_canoes <= 30 * 120
# total hours required for luxury canoes
problem += 2 * num_simple_canoes + 1 * num_luxury_canoes <= 30 * 120
# total hours required for all canoes
problem += 2 * num_simple_canoes + 4 * num_luxury_canoes <= 30 * 120
# luxury canoes constraint
problem  += 3*num_luxury_canoes >= num_luxury_canoes + num_simple_canoes # problem += num_luxury_canoes >= 1/3 * (num_simple_canoes + num_luxury_canoes)
problem += num_simple_canoes + num_luxury_canoes <= 200

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of simple canoes to produce:", num_simple_canoes.value())
print("The number of luxury canoes to produce:", num_luxury_canoes.value())
print("The maximum overall net profit:", objective.value())
print("## end solving")