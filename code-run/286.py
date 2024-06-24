from pulp import *

# Define the decision variables
num_dense_lifts = LpVariable("NumDenseLifts", lowBound=0, cat='Integer')
num_loose_lifts = LpVariable("NumLooseLifts", lowBound=5, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("SkiResortProblem", LpMinimize)

# Define the objective function
problem += num_dense_lifts + num_loose_lifts

# Define the constraints
problem += 45 * num_dense_lifts + 20 * num_loose_lifts >= 1000
problem += 30 * num_dense_lifts + 22 * num_loose_lifts <= 940

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of densely-seated ski lifts:", num_dense_lifts.value())
print("The number of loosely-seated ski lifts:", num_loose_lifts.value())
print("Total number of ski lifts:", value(problem.objective))
print("## end solving")