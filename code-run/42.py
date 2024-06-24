from pulp import *

# Define the variables
num_beans = LpVariable("NumBeans", lowBound=0, cat='Integer')
num_onions = LpVariable("NumOnions", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("BurritoProblem", LpMinimize)
objective = 6 * num_beans + 8 * num_onions
problem += objective

# Define the constraints
problem += 10 * num_beans + 2 * num_onions >= 110
problem += 3 * num_beans + 6 * num_onions >= 80

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of units of beans:", value(num_beans))
print("The number of units of onions:", value(num_onions))
print("The minimum cost:", value(objective))
print("## end solving")