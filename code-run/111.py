from pulp import *

# Define the decision variables
# number of Oil Max containers
num_oil_max = LpVariable("NumOilMax", lowBound=0, cat='Integer')
# number of Oil Max Pro containers
num_oil_max_pro = LpVariable("NumOilMaxPro", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("CarOilProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 10 * num_oil_max + 15 * num_oil_max_pro
problem += objective

# Define the constraints
# total amount of substance A
problem += 46 * num_oil_max + 13 * num_oil_max_pro <= 1345
# total amount of substance B
problem += 43 * num_oil_max + 4 * num_oil_max_pro <= 346
# total amount of substance C
problem += 56 * num_oil_max + 45 * num_oil_max_pro <= 1643

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of Oil Max containers:", num_oil_max.value())
print("The number of Oil Max Pro containers:", num_oil_max_pro.value())
print("The total profit:", objective.value())
print("## end solving")