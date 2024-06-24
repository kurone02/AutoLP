from pulp import *

# Define the decision variables
sweatshirts_f = LpVariable("SweatshirtsF", lowBound=0, cat='Integer')
sweatshirts_bf = LpVariable("SweatshirtsBF", lowBound=0, cat='Integer')
tshirts_f = LpVariable("TshirtsF", lowBound=0, cat='Integer')
tshirts_bf = LpVariable("TshirtsBF", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("ShirtProductionProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 90 * sweatshirts_f + 125 * sweatshirts_bf + 45 * tshirts_f + 65 * tshirts_bf
problem += objective

# Define the constraints
# total processing time
problem += 0.10 * sweatshirts_f + 0.25 * sweatshirts_bf + 0.08 * tshirts_f + 0.21 * tshirts_bf <= 72
# total cost
problem += 36 * sweatshirts_f + 125 * sweatshirts_bf + 25 * tshirts_f + 48 * tshirts_bf <= 25000
# total product boxes
problem += sweatshirts_f + sweatshirts_bf + tshirts_f + tshirts_bf <= 1200
# total sweatshirts and T-shirts in stock
problem += sweatshirts_f + sweatshirts_bf + tshirts_f + tshirts_bf <= 500

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of sweatshirts with front printing to produce:", sweatshirts_f.value())
print("The number of sweatshirts with back and front printing to produce:", sweatshirts_bf.value())
print("The number of T-shirts with front printing to produce:", tshirts_f.value())
print("The number of T-shirts with back and front printing to produce:", tshirts_bf.value())
print("The maximum profit:", objective.value())
print("## end solving")