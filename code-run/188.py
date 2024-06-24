from pulp import *

# Define the decision variables
# number of units of product 1 to produce
num_product_1 = LpVariable("NumProduct1", lowBound=0, cat='Integer')
# number of units of product 2 to produce
num_product_2 = LpVariable("NumProduct2", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("ManufacturerProfitMaximization", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 2 * num_product_1 + 5 * num_product_2
problem += objective

# Define the constraints
# total raw material available
problem += 3 * num_product_1 + 6 * num_product_2 <= 120
# setup cost for product 1
problem += 10 * num_product_1 <= 1000
# setup cost for product 2
problem += 20 * num_product_2 <= 1000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of units of product 1 to produce:", num_product_1.value())
print("The number of units of product 2 to produce:", num_product_2.value())
print("The total profit:", objective.value())
print("## end solving")