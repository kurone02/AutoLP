from pulp import *

# Define the decision variables
# number of units of product A
num_units_A = LpVariable("NumUnitsA", lowBound=0, cat='Integer')
# number of units of product B
num_units_B = LpVariable("NumUnitsB", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("CompanyProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 3 * num_units_A + 4 * num_units_B
problem += objective

# Define the constraints
# R constraint
problem += 6 * num_units_A + 12 * num_units_B <= 900
# S constraint
problem += 7.5 * num_units_A + 4.5 * num_units_B <= 675
# labor constraint
problem += 9 * num_units_A + 6 * num_units_B <= 1200

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of units of product A to produce:", num_units_A.value())
print("The number of units of product B to produce:", num_units_B.value())
print("The maximum profit:", objective.value())
print("## end solving")