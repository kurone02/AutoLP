from pulp import *

# Define the decision variables
# number of wide trails
num_wide_trails = LpVariable("NumWideTrails", lowBound=0, cat='Integer')
# number of narrow trails
num_narrow_trails = LpVariable("NumNarrowTrails", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("ParkTrailsProblem", LpMinimize)

# Define the objective function
# minimize the total garbage produced
objective = 6 * num_wide_trails + 3 * num_narrow_trails
problem += objective

# Define the constraints
# total visitors
problem += 50 * num_wide_trails + 20 * num_narrow_trails <= 225
# maximum number of wide trails
problem += num_wide_trails <= 3
# non-negative number of trails
problem += num_wide_trails >= 0
problem += num_narrow_trails >= 0

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of wide trails:", num_wide_trails.value())
print("The number of narrow trails:", num_narrow_trails.value())
print("The total amount of garbage produced:", objective.value())
print("## end solving")