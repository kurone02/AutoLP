from pulp import *

# Define the decision variables
num_workers_line1 = LpVariable("NumWorkersLine1", lowBound=0, cat='Integer')
num_workers_line2 = LpVariable("NumWorkersLine2", lowBound=0, cat='Integer')

# Define the question as a minimum or maximum problem
problem = LpProblem("GlueProductionProblem", LpMinimize)

# Define the objective function
objective = 1000 * (num_workers_line1 >= 1 + 0) + 500 * num_workers_line1 + 2000 * (num_workers_line2 >= 1 + 0) + 900 * num_workers_line2
problem += objective

# Define the constraints
problem += 20 * num_workers_line1 + 50 * num_workers_line2 >= 120
problem += 30 * num_workers_line1 + 35 * num_workers_line2 >= 150
problem += 40 * num_workers_line1 + 45 * num_workers_line2 >= 200
problem += num_workers_line1 <= 7
problem += num_workers_line2 <= 7

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of workers on production line 1:", num_workers_line1.value())
print("The number of workers on production line 2:", num_workers_line2.value())
print("The total cost:", objective.value())
print("## end solving")