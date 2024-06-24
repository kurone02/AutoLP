from pulp import *

# Define the decision variables
# number of scooters
num_scooters = LpVariable("NumScooters", lowBound=0, cat='Integer')
# number of rickshaws
num_rickshaws = LpVariable("NumRickshaws", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("ThemeParkProblem", LpMinimize)

# Define the objective function
# minimize the total number of scooters used
problem += num_scooters

# Define the constraints
# total number of people transported
problem += 2 * num_scooters + 3 * num_rickshaws >= 300
# maximum percentage of vehicles that can be rickshaws
problem += num_rickshaws <= 0.4 * (num_scooters + num_rickshaws)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of scooters:", num_scooters.value())
print("The number of rickshaws:", num_rickshaws.value())
print("The total number of vehicles used:", value(num_scooters) + value(num_rickshaws))
print("## end solving")