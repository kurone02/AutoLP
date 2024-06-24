from pulp import *

# Define the variables
num_hours_process1 = LpVariable("NumHoursProcess1", lowBound=0, cat='Continuous')
num_hours_process2 = LpVariable("NumHoursProcess2", lowBound=0, cat='Continuous')

# Define the problem
problem = LpProblem("DrugCompanyProblem", LpMinimize)
objective = num_hours_process1 + num_hours_process2
problem += objective

# Define the constraints
problem += 50 * num_hours_process1 + 60 * num_hours_process2 <= 2000
problem += 35 * num_hours_process1 + 50 * num_hours_process2 >= 1200
problem += 12 * num_hours_process1 + 30 * num_hours_process2 >= 1200

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of hours to run process 1:", value(num_hours_process1))
print("The number of hours to run process 2:", value(num_hours_process2))
print("The total time:", value(objective))
print("## end solving")