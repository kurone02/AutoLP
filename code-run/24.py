from pulp import *

# Define the decision variables
# number of acres of apple trees
num_acres_apple = LpVariable("NumAcresApple", lowBound=0, cat='Integer')
# number of acres of peach trees
num_acres_peach = LpVariable("NumAcresPeach", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("FarmProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 15 * num_acres_apple + 25 * num_acres_peach
problem += objective

# Define the constraints
# total cost of saplings
problem += 50 * num_acres_apple + 80 * num_acres_peach <= 30000
# total time for maintenance
problem += 3 * num_acres_apple + 5 * num_acres_peach <= 600
# total acres
problem += num_acres_apple + num_acres_peach <= 4000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of acres for apple trees:", num_acres_apple.value())
print("The number of acres for peach trees:", num_acres_peach.value())
print("The maximum profit:", objective.value())
print("## end solving")