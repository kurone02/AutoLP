from pulp import *

# Define the decision variables
# number of hamburgers
num_hamburgers = LpVariable("NumHamburgers", lowBound=0, cat='Integer')
# number of chicken wraps
num_wraps = LpVariable("NumWraps", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("DietProblem", LpMinimize)

# Define the objective function
# minimize the total cost
objective = 6.5 * num_hamburgers + 4 * num_wraps
problem += objective

# Define the constraints
# total calories
problem += 800 * num_hamburgers + 450 * num_wraps >= 2200
# total protein
problem += 19 * num_hamburgers + 12 * num_wraps >= 50
# total carbs
problem += 20 * num_hamburgers + 10 * num_wraps >= 70

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of hamburgers:", num_hamburgers.value())
print("The number of chicken wraps:", num_wraps.value())
print("The minimum cost:", objective.value())
print("## end solving")