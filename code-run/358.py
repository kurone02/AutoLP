from pulp import *

# Define the decision variables
# number of full-time staff
num_full_time = LpVariable("NumFullTime", lowBound=0, cat='Integer')
# number of part-time staff
num_part_time = LpVariable("NumPartTime", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("StaffHiringProblem", LpMinimize)

# Define the objective function
# minimize the total number of staff
objective = num_full_time + num_part_time
problem += objective

# Define the constraints
# total hours of labor
problem += 40 * num_full_time + 15 * num_part_time <= 1000
# total budget
problem += 1280 * num_full_time + 450 * num_part_time <= 31500

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of full-time staff to hire:", num_full_time.value())
print("The number of part-time staff to hire:", num_part_time.value())
print("The total number of staff hired:", objective.value())
print("## end solving")