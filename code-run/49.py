from pulp import *

# Define the decision variables
x1 = LpVariable("x1", lowBound=0, cat='Integer')
x2 = LpVariable("x2", lowBound=0, cat='Integer')

# Define the question as a minimum or maximum problem
problem = LpProblem("HotDogProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 3 * x1 + 5 * x2
problem += objective

# Define the constraints
# total number of hot-dogs
problem += x1 + x2 <= 300
# regular hot-dogs demand
problem += x1 <= 100
# premium hot-dogs demand
problem += x2 <= 250

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of regular hot-dogs to make:", x1.value())
print("The number of premium hot-dogs to make:", x2.value())
print("Maximum profit per day:", objective.value())
print("## end solving")