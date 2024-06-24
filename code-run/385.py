from pulp import *

# Define the variables
num_product_A = LpVariable("NumProductA", lowBound=0, cat='Integer')
num_product_B = LpVariable("NumProductB", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("CompanyProfitMaximization", LpMaximize)
objective = 3 * num_product_A + 4 * num_product_B
problem += objective

# Define the constraints
problem += 6 * num_product_A + 12 * num_product_B <= 900
problem += 7.5 * num_product_A + 4.5 * num_product_B <= 675
problem += 9 * num_product_A + 6 * num_product_B <= 1200

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of units of product A to produce:", value(num_product_A))
print("The number of units of product B to produce:", value(num_product_B))
print("The maximum profit:", value(objective))
print("## end solving")