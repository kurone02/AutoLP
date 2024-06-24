from pulp import *

# Define the decision variables
# number of sliding doors
num_sliding_doors = LpVariable("NumSlidingDoors", lowBound=120, upBound=210, cat='Integer')
# number of windows
num_windows = LpVariable("NumWindows", lowBound=110, upBound=170, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("GlassCompanyProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 30 * num_sliding_doors + 25 * num_windows
problem += objective

# Define the constraints
# minimum orders
# problem += num_sliding_doors >= 120
# problem += num_windows >= 110
# maximum capacities
# problem += num_sliding_doors <= 210
# problem += num_windows <= 170
# contract
problem += num_sliding_doors + num_windows >= 250

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of sliding doors to make:", num_sliding_doors.value())
print("The number of windows to make:", num_windows.value())
print("Total profit per day:", objective.value())
print("## end solving")