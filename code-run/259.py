from pulp import *

# Define the decision variables
# number of refrigerators to sell
num_refrigerators = LpVariable("NumRefrigerators", lowBound=0, cat='Integer')
# number of stoves to sell
num_stoves = LpVariable("NumStoves", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("ApplianceCompanyProfitMaximization", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 400 * num_refrigerators + 260 * num_stoves
problem += objective

# Define the constraints
# mover time constraint
problem += 60 * num_refrigerators + 45 * num_stoves <= 20000
# setup time constraint
problem += 20 * num_refrigerators + 25 * num_stoves <= 13000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of refrigerators to sell:", num_refrigerators.value())
print("The number of stoves to sell:", num_stoves.value())
print("The maximum profit:", objective.value())
print("## end solving")