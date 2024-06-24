from pulp import *

# Define the variables
num_super_two_fresno = LpVariable("NumSuperTwoFresno", lowBound=0, cat='Integer')
num_super_two_dearborn = LpVariable("NumSuperTwoDearborn", lowBound=0, cat='Integer')
num_green_grow_fresno = LpVariable("NumGreenGrowFresno", lowBound=0, cat='Integer')
num_green_grow_dearborn = LpVariable("NumGreenGrowDearborn", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("FertilizerProduction", LpMaximize)
objective = (9 - 2) * (num_super_two_fresno + num_super_two_dearborn) + (7 - 2) * (num_green_grow_fresno + num_green_grow_dearborn)
problem += objective

# Define the constraints
problem += num_super_two_fresno + num_super_two_dearborn + num_green_grow_fresno + num_green_grow_dearborn <= 5000 + 6000
problem += num_super_two_fresno + num_super_two_dearborn <= 6000
problem += num_green_grow_fresno + num_green_grow_dearborn <= 7000
problem += 2 * (num_super_two_fresno + num_super_two_dearborn + num_green_grow_fresno + num_green_grow_dearborn) <= 45000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of pounds of Super Two produced at Fresno:", num_super_two_fresno.value())
print("The number of pounds of Super Two produced at Dearborn:", num_super_two_dearborn.value())
print("The number of pounds of Green Grow produced at Fresno:", num_green_grow_fresno.value())
print("The number of pounds of Green Grow produced at Dearborn:", num_green_grow_dearborn.value())
print("The maximum profit:", objective.value())
print("## end solving")