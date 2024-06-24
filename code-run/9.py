from pulp import *

# Define the decision variables
# number of pies
num_pies = LpVariable("NumPies", lowBound=30, cat='Integer')
# number of tarts
num_tarts = LpVariable("NumTarts", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("BakeryProfitMaximization", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 8 * num_pies + 5 * num_tarts
problem += objective

# Define the constraints
# total blueberries available
problem += 5 * num_pies + 3 * num_tarts <= 1000
# at least three times the number of pies
problem += num_tarts >= 3 * num_pies
# at least 30 pies
problem += num_pies >= 30

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of pies to make:", num_pies.value())
print("The number of tarts to make:", num_tarts.value())
print("The maximum profit:", objective.value())
print("## end solving")