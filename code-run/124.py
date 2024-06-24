from pulp import *

# Define the decision variables
num_processA = LpVariable("ProcessA", lowBound=0, cat='Integer')
num_processB = LpVariable("ProcessB", lowBound=0, cat='Integer')

# Define the question as a minimum or maximum problem
problem = LpProblem("CoinPlatingProblem", LpMaximize)

# Define the objective function
problem += 5 * num_processA + 7 * num_processB

# Define the constraints
problem += 3 * num_processA + 5 * num_processB <= 500
problem += 2 * num_processA + 3 * num_processB <= 300

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of Process A:", num_processA.value())
print("The number of Process B:", num_processB.value())
print("The total number of coins that can be plated:", value(problem.objective))
print("## end solving")