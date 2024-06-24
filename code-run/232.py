from pulp import *

# Define the decision variables
# number of small bins
num_small_bins = LpVariable("NumSmallBins", lowBound=0, cat='Integer')
# number of large bins
num_large_bins = LpVariable("NumLargeBins", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("RecyclingProblem", LpMaximize)

# Define the objective function
# maximize the total amount of recycling material collected
objective = 25 * num_small_bins + 60 * num_large_bins
problem += objective

# Define the constraints
# total number of workers
problem += 2 * num_small_bins + 5 * num_large_bins <= 100
# number of small bins must be three times the number of large bins
problem += num_small_bins == 3 * num_large_bins
# at least 10 small bins must be used
problem += num_small_bins >= 10
# at least 4 large bins must be used
problem += num_large_bins >= 4

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of small bins:", num_small_bins.value())
print("The number of large bins:", num_large_bins.value())
print("The total amount of recycling material collected:", objective.value())
print("## end solving")