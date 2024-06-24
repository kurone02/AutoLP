from pulp import *

# Define the decision variables
# number of wraps to make
num_wraps = LpVariable("NumWraps", lowBound=0, cat='Integer')
# number of platters to make
num_platters = LpVariable("NumPlatters", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("FastFoodProblem", LpMinimize)

# Define the objective function
# minimize the total production time
objective = 10 * num_wraps + 8 * num_platters
problem += objective

# Define the constraints
# meat constraint
problem += 5 * num_wraps + 7 * num_platters >= 3000
# rice constraint
problem += 3 * num_wraps + 5 * num_platters >= 2500
# wraps to platter ratio constraint
problem += num_wraps >= 3 * num_platters

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of wraps:", num_wraps.value())
print("The number of platters:", num_platters.value())
print("The total production time (in minutes):", objective.value())
print("## end solving")