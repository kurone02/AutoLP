from pulp import *

# Define the decision variables
# number of A400 keyboards to produce each week
num_A400 = LpVariable("NumA400", lowBound=0, cat='Integer')
# number of P500 keyboards to produce each week
num_P500 = LpVariable("NumP500", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("CuriousElectronicsProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 35 * num_A400 + 80 * num_P500
problem += objective

# Define the constraints
# total labour hours
problem += 5 * num_A400 + 9 * num_P500 <= 45
# A400 keyboards constraint
problem += num_A400 >= 3 * num_P500

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("Number of A400 keyboards to produce each week:", num_A400.value())
print("Number of P500 keyboards to produce each week:", num_P500.value())
print("Maximum profit:", objective.value())
print("## end solving")