from pulp import *

# Define the decision variables
# number of SUVs to produce
num_SUVs = LpVariable("NumSUVs", lowBound=0, cat='Integer')
# number of sedans to produce
num_sedans = LpVariable("NumSedans", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("CarProductionProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 10000 * num_SUVs + 9000 * num_sedans
problem += objective

# Define the constraints
# total time on the manufacturing line
problem += 200 * num_SUVs + 150 * num_sedans <= 20000
# total time for testing
problem += 120 * num_SUVs + 100 * num_sedans <= 10000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of SUVs to produce:", num_SUVs.value())
print("The number of sedans to produce:", num_sedans.value())
print("The maximum total profit:", objective.value())
print("## end solving")