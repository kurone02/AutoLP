from pulp import *

# Define the variables
num_alpha_bottles = LpVariable("NumAlphaBottles", lowBound=0, cat='Integer')
num_omega_bottles = LpVariable("NumOmegaBottles", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("DietProblem", LpMinimize)
objective = 20 * num_alpha_bottles + 15 * num_omega_bottles
problem += objective

# Define the constraints
problem += 30 * num_alpha_bottles + 20 * num_omega_bottles >= 100
problem += 350 * num_alpha_bottles + 300 * num_omega_bottles >= 2000
problem += num_omega_bottles <= 0.35 * (num_alpha_bottles + num_omega_bottles)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of alpha brand bottles:", value(num_alpha_bottles))
print("The number of omega brand bottles:", value(num_omega_bottles))
print("The total sugar intake:", value(objective))
print("## end solving")