from pulp import *

# Define the decision variables
# number of golf carts
num_golf_carts = LpVariable("GolfCarts", lowBound=0, cat='Integer')
# number of pull carts
num_pull_carts = LpVariable("PullCarts", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("GolfCartProblem", LpMinimize)

# Define the objective function
# minimize the total number of carts
problem += num_golf_carts + num_pull_carts

# Define the constraints
# capacity constraint for golf carts
problem += num_golf_carts * 4 + num_pull_carts * 1 >= 80
# maximum percentage of golf carts
problem += num_golf_carts <= 0.6 * (num_golf_carts + num_pull_carts)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of golf carts to use:", num_golf_carts.value())
print("The number of pull carts to use:", num_pull_carts.value())
print("The total number of carts used:", value(problem.objective))
print("## end solving")