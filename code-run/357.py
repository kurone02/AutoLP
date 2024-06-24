from pulp import *

# Define the variables
sq_ft_heavy = LpVariable("SquareFeetHeavy", lowBound=0, cat='Integer')
sq_ft_gas = LpVariable("SquareFeetGas", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("LandscapingProblem", LpMinimize)

# Define the objective function
objective = 2 * sq_ft_heavy + 5 * sq_ft_gas
problem += objective

# Define the constraints
problem += sq_ft_heavy + sq_ft_gas <= 100
problem += 3 * sq_ft_heavy + 2 * sq_ft_gas <= 450
problem += 12 * sq_ft_heavy + 10 * sq_ft_gas <= 2000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("Square feet for heavy-duty yard machine:", sq_ft_heavy.value())
print("Square feet for gas lawn mower:", sq_ft_gas.value())
print("Total time required (seconds):", objective.value())
print("## end solving")