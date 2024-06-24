from pulp import *

# Define the decision variables
num_sweatshirts_F = LpVariable("NumSweatshirtsF", lowBound=0, cat='Integer')
num_sweatshirts_B_F = LpVariable("NumSweatshirtsBF", lowBound=0, cat='Integer')
num_tshirts_F = LpVariable("NumTshirtsF", lowBound=0, cat='Integer')
num_tshirts_B_F = LpVariable("NumTshirtsBF", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("TshirtManufacturingProblem", LpMaximize)

# Define the objective function
objective = 90 * num_sweatshirts_F + 125 * num_sweatshirts_B_F + 45 * num_tshirts_F + 65 * num_tshirts_B_F
problem += objective

# Define the constraints
problem += 0.1 * num_sweatshirts_F + 0.25 * num_sweatshirts_B_F + 0.08 * num_tshirts_F + 0.21 * num_tshirts_B_F <= 72
problem += 36 * num_sweatshirts_F + 48 * num_sweatshirts_B_F + 25 * num_tshirts_F + 35 * num_tshirts_B_F <= 25000
problem += num_sweatshirts_F + num_sweatshirts_B_F + 3 * num_tshirts_F + 3 * num_tshirts_B_F <= 1200
problem += num_sweatshirts_F + num_sweatshirts_B_F + 500 <= 1200
problem += num_tshirts_F + num_tshirts_B_F + 500 <= 1200

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of sweatshirts with front printing to produce:", num_sweatshirts_F.value())
print("The number of sweatshirts with back and front printing to produce:", num_sweatshirts_B_F.value())
print("The number of T-shirts with front printing to produce:", num_tshirts_F.value())
print("The number of T-shirts with back and front printing to produce:", num_tshirts_B_F.value())
print("The maximum profit:", objective.value())
print("## end solving")