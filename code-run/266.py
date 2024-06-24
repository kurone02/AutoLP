from pulp import *

# Define the decision variables
# number of servings of health supplement A
num_servings_A = LpVariable("NumServingsA", lowBound=0, cat='Integer')
# number of servings of health supplement B
num_servings_B = LpVariable("NumServingsB", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("HealthSupplementProblem", LpMinimize)

# Define the objective function
# minimize the total cost
objective = 14 * num_servings_A + 25 * num_servings_B
problem += objective

# Define the constraints
# total calcium
problem += 30 * num_servings_A + 60 * num_servings_B >= 400
# total magnesium
problem += 50 * num_servings_A + 10 * num_servings_B >= 50

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of servings for health supplement A:", num_servings_A.value())
print("The number of servings for health supplement B:", num_servings_B.value())
print("The minimum daily cost:", objective.value())
print("## end solving")