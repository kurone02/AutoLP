from pulp import *

# Define the decision variables
# number of small boxes
num_small_boxes = LpVariable("NumSmallBoxes", lowBound=0, cat='Integer')
# number of large boxes
num_large_boxes = LpVariable("NumLargeBoxes", lowBound=5, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("MaskMakingProblem", LpMinimize)

# Define the objective function
# minimize the total number of boxes
objective = num_small_boxes + num_large_boxes
problem += objective

# Define the constraints
# total masks distributed
problem += 25 * num_small_boxes + 45 * num_large_boxes >= 750
# three times as many small boxes as large boxes
problem += num_small_boxes >= 3 * num_large_boxes
# at least 5 large boxes
problem += num_large_boxes >= 5

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of small boxes:", num_small_boxes.value())
print("The number of large boxes:", num_large_boxes.value())
print("The total number of boxes:", objective.value())
print("## end solving")