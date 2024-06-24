from pulp import *

# Define the variables
num_tacos = LpVariable("NumTacos", lowBound=50, upBound=80, cat='Integer')
num_burritos = LpVariable("NumBurritos", lowBound=30, upBound=50, cat='Integer')

# Define the problem
problem = LpProblem("FoodTruckProblem", LpMaximize)
objective = 3 * num_tacos + 6 * num_burritos
problem += objective

# Define the constraints
problem += num_tacos + num_burritos <= 100

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of tacos sold:", value(num_tacos))
print("The number of burritos sold:", value(num_burritos))
print("Total profit:", value(objective))
print("## end solving")