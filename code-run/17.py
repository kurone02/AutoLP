from pulp import *

# Define the decision variables
# number of regular donuts
num_regular = LpVariable("NumRegularDonuts", lowBound=0, cat='Integer')
# number of jelly-filled donuts
num_jelly = LpVariable("NumJellyDonuts", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("DonutProfitProblem", LpMaximize)

# Define the objective function
# maximize the total monthly profit
objective = 2 * num_regular + 3 * num_jelly
problem += objective

# Define the constraints
# total donuts sold
problem += num_regular + num_jelly <= 1000
# total cost
problem += 4 * num_regular + 6 * num_jelly <= 5000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of regular donuts:", num_regular.value())
print("The number of jelly-filled donuts:", num_jelly.value())
print("The total monthly profit:", objective.value())
print("## end solving")