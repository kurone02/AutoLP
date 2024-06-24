from pulp import *

# Define the decision variables
num_workers_line1 = LpVariable("NumWorkersLine1", lowBound=0, upBound=7, cat='Integer')
num_workers_line2 = LpVariable("NumWorkersLine2", lowBound=0, upBound=7, cat='Integer')

# Define the problem
problem = LpProblem("GlueCoProblem", LpMinimize)
objective = 1000 + 500 * num_workers_line1 + 2000 + 900 * num_workers_line2
problem += objective

# Define the constraints
problem += num_workers_line1 <= 7
problem += num_workers_line2 <= 7
problem += 20 * num_workers_line1 + 50 * num_workers_line2 >= 120
problem += 30 * num_workers_line1 + 35 * num_workers_line2 >= 150
problem += 40 * num_workers_line1 + 45 * num_workers_line2 >= 200

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of workers on production line 1:", num_workers_line1.value())
print("The number of workers on production line 2:", num_workers_line2.value())
print("The total cost:", objective.value())
print("## end solving")