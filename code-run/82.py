from pulp import *

# Define the decision variables
# number of acres of apples
num_acres_apples = LpVariable("AcresApples", lowBound=5, cat='Integer')
# number of acres of pears
num_acres_pears = LpVariable("AcresPears", lowBound=10, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("FarmerProfitProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 2 * num_acres_apples + 4 * num_acres_pears
problem += objective

# Define the constraints
# minimum acres for apples
problem += num_acres_apples >= 5
# minimum acres for pears
problem += num_acres_pears >= 10
# total acres
problem += num_acres_apples + num_acres_pears <= 50
# limitation in his workforce allow him to grow at most twice the amount of pears as apples
problem += num_acres_pears <= 2 * num_acres_apples

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of acres for apples:", num_acres_apples.value())
print("The number of acres for pears:", num_acres_pears.value())
print("The total profit:", objective.value())
print("## end solving")