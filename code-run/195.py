from pulp import *

# Define the decision variables
num_apple_butter = LpVariable("NumAppleButter", lowBound=0, cat='Integer')
num_applesauce = LpVariable("NumApplesauce", lowBound=0, cat='Integer')
num_apple_jelly = LpVariable("NumAppleJelly", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("FarmProductionProblem", LpMaximize)

# Define the objective function
objective = 190 * num_apple_butter + 170 * num_applesauce + 155 * num_apple_jelly
problem += objective

# Define the constraints
problem += 3.5 * num_apple_butter + 5.2 * num_applesauce + 2.8 * num_apple_jelly <= 500
problem += 1.2 * num_apple_butter + 0.8 * num_applesauce + 1.5 * num_apple_jelly <= 240
problem += 40 * num_apple_butter + 55 * num_applesauce + 20 * num_apple_jelly <= 6500

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("Number of Apple Butter batches to produce:", num_apple_butter.value())
print("Number of Apple Sauce batches to produce:", num_applesauce.value())
print("Number of Apple Jelly batches to produce:", num_apple_jelly.value())
print("Total Revenue:", objective.value())
print("## end solving")