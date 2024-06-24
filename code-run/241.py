from pulp import *

# Define the variables
num_balloons = LpVariable("NumBalloons", lowBound=0, cat='Integer')
num_gondolas = LpVariable("NumGondolas", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("TouristSpotProblem", LpMinimize)
objective = 10 * num_balloons + 15 * num_gondolas
problem += objective

# Define the constraints
problem += 4 * num_balloons + 6 * num_gondolas >= 70
problem += num_balloons <= 10
problem += 6 * num_gondolas <= 40

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of hot air balloon rides:", value(num_balloons))
print("The number of gondola lift rides:", value(num_gondolas))
print("The total pollution produced:", value(objective))
print("## end solving")