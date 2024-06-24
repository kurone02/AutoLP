from pulp import *

# Define the decision variables
# number of hams to produce
num_hams = LpVariable("NumHams", lowBound=0, cat='Integer')
# number of pork ribs to produce
num_ribs = LpVariable("NumRibs", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("MeatProcessingProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 150 * num_hams + 300 * num_ribs
problem += objective

# Define the constraints
# total time on the meat slicer
problem += 4 * num_hams + 2 * num_ribs <= 4000
# total time on the meat packer
problem += 2.5 * num_hams + 3.5 * num_ribs <= 4000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of batches of hams:", num_hams.value())
print("The number of batches of pork ribs:", num_ribs.value())
print("The total profit:", objective.value())
print("## end solving")