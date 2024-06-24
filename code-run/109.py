from pulp import *

# Define the decision variables
# number of long desks
num_long_desks = LpVariable("NumLongDesks", lowBound=0, cat='Integer')
# number of short desks
num_short_desks = LpVariable("NumShortDesks", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("OfficeDeskProblem", LpMaximize)

# Define the objective function
# maximize the total seating availability
objective = 6 * num_long_desks + 2 * num_short_desks
problem += objective

# Define the constraints
# total cost
problem += 300 * num_long_desks + 100 * num_short_desks <= 2000
# total square feet of desks
problem += 10 * num_long_desks + 4 * num_short_desks <= 200

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of long desks:", num_long_desks.value())
print("The number of short desks:", num_short_desks.value())
print("The seating availability:", objective.value())
print("## end solving")