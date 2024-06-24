from pulp import *

# Define the variables
num_led = LpVariable("NumLED", lowBound=0, cat='Integer')
num_neon = LpVariable("NumNeon", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("SignCompanyProblem", LpMaximize)

# Define the objective function
objective = 1500 * num_led + 1450 * num_neon
problem += objective

# Define the constraints
problem += num_led <= 3
problem += num_neon <= 4
problem += num_led + num_neon <= 7

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of LED signs made:", num_led.value())
print("The number of neon signs made:", num_neon.value())
print("The total profit:", objective.value())
print("## end solving")