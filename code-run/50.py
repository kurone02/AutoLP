from pulp import *

# Define the decision variables
# number of acres of oranges to grow
num_oranges = LpVariable("NumOranges", lowBound=60, cat='Integer')
# number of acres of grapefruits to grow
num_grapefruits = LpVariable("NumGrapefruits", lowBound=50, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("FarmerProfitProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 200 * num_oranges + 220 * num_grapefruits
problem += objective

# Define the constraints
# total acres to grow
problem += num_oranges + num_grapefruits <= 200
# at least 60 acres of oranges
problem += num_oranges >= 60
# at least 50 acres of grapefruits
problem += num_grapefruits >= 50
# no more than twice the amount of grapefruits as oranges
problem += num_grapefruits <= 2 * num_oranges

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of acres of oranges to grow:", num_oranges.value())
print("The number of acres of grapefruits to grow:", num_grapefruits.value())
print("Total profit:", objective.value())
print("## end solving")