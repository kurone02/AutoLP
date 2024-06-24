from pulp import *

# Define the decision variables
# number of desk lamps
num_desk_lamps = LpVariable("NumDeskLamps", lowBound=30, upBound=150, cat='Integer')
# number of night lamps
num_night_lamps = LpVariable("NumNightLamps", lowBound=50, upBound=180, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("LightingCompanyProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 5 * num_desk_lamps + 8 * num_night_lamps
problem += objective

# Define the constraints
# at least 30 desk lamps
# at least 50 night lamps
# at most 150 desk lamps
# at most 180 night lamps
# a minimum of 100 lamps
problem += num_desk_lamps + num_night_lamps >= 100

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of desk lamps:", num_desk_lamps.value())
print("The number of night lamps:", num_night_lamps.value())
print("The total profit:", objective.value())
print("## end solving")