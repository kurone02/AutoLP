from pulp import *

# Define the decision variables
# number of strawberry cookies
num_strawberry = LpVariable("StrawberryCookies", lowBound=0, cat='Integer')
# number of sugar cookies
num_sugar = LpVariable("SugarCookies", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("ZetaBakeryProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 5.5 * num_strawberry + 12 * num_sugar
problem += objective

# Define the constraints
# total cookies produced
problem += num_strawberry + num_sugar <= 100
# demand for strawberry cookies
problem += num_strawberry <= 100
# demand for sugar cookies
problem += num_sugar <= 80

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of strawberry cookies:", num_strawberry.value())
print("The number of sugar cookies:", num_sugar.value())
print("The total profit:", objective.value())
print("## end solving")