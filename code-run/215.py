from pulp import *

# Define the decision variables
# number of manual slicers
num_manual_slicers = LpVariable("NumManualSlicers", lowBound=0, cat='Integer')
# number of automatic slicers
num_automatic_slicers = LpVariable("NumAutomaticSlicers", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("ButcherShopProblem", LpMinimize)

# Define the objective function
# minimize the total number of slicers
objective = num_manual_slicers + num_automatic_slicers
problem += objective

# Define the constraints
# cutting constraint
problem += 5 * num_manual_slicers + 8 * num_automatic_slicers >= 50
# grease constraint
problem += 3 * num_manual_slicers + 6 * num_automatic_slicers <= 40
# number of slicers constraint
problem += num_manual_slicers <= num_automatic_slicers

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of manual slicers:", num_manual_slicers.value())
print("The number of automatic slicers:", num_automatic_slicers.value())
print("The minimum total number of slicers:", objective.value())
print("## end solving")