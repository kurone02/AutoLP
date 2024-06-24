from pulp import *

# Define the decision variables
# number of workers on line 1
num_workers_line1 = LpVariable("WorkersLine1", lowBound=0, cat='Integer')
# number of workers on line 2
num_workers_line2 = LpVariable("WorkersLine2", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("GlueCoProblem", LpMinimize)

# Define the objective function
# minimize the total cost
objective = 500 * num_workers_line1 + 900 * num_workers_line2 + 1000 + 2000
problem += objective

# Define the constraints
# maximum workers on each line
problem += num_workers_line1 <= 7
problem += num_workers_line2 <= 7
# production constraints
problem += 20 * num_workers_line1 + 30 * num_workers_line2 >= 120
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