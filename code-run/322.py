from pulp import *

# Define the decision variables
# number of wide pipes
num_wide_pipes = LpVariable("NumWidePipes", lowBound=5, cat='Integer')
# number of narrow pipes
num_narrow_pipes = LpVariable("NumNarrowPipes", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("WaterTransportProblem", LpMinimize)

# Define the objective function
# minimize the total number of pipes
objective = num_wide_pipes + num_narrow_pipes
problem += objective

# Define the constraints
# water transport constraint
problem += 25 * num_wide_pipes + 15 * num_narrow_pipes >= 900
# wide pipe constraint
problem += num_wide_pipes >= 5
# ratio constraint
problem  += 3*num_wide_pipes <= num_narrow_pipes # problem += num_wide_pipes <= 1/3 * num_narrow_pipes

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of wide pipes:", num_wide_pipes.value())
print("The number of narrow pipes:", num_narrow_pipes.value())
print("The total number of pipes:", objective.value())
print("## end solving")