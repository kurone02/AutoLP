from pulp import *

# Define the decision variables
num_super_two_fresno = LpVariable("SuperTwoFresno", lowBound=0, cat='Integer')
num_super_two_dearborn = LpVariable("SuperTwoDearborn", lowBound=0, cat='Integer')
num_green_grow_fresno = LpVariable("GreenGrowFresno", lowBound=0, cat='Integer')
num_green_grow_dearborn = LpVariable("GreenGrowDearborn", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("FertilizerProblem", LpMaximize)

# Define the objective function
objective = (9 * num_super_two_fresno + 9 * num_super_two_dearborn + 7 * num_green_grow_fresno + 7 * num_green_grow_dearborn) - (2 * num_super_two_fresno + 4 * num_super_two_dearborn + 2 * num_green_grow_fresno + 3 * num_green_grow_dearborn)
problem += objective

# Define the constraints
problem += num_super_two_fresno + num_green_grow_fresno <= 5000
problem += num_super_two_dearborn + num_green_grow_dearborn <= 6000
problem += num_super_two_fresno + num_super_two_dearborn <= 6000
problem += num_green_grow_fresno + num_green_grow_dearborn <= 7000
problem += 2 * num_super_two_fresno + 4 * num_super_two_dearborn + 2 * num_green_grow_fresno + 3 * num_green_grow_dearborn <= 45000

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