from pulp import *

# Define the variables
time_beam1 = LpVariable("TimeBeam1", lowBound=0, cat='Continuous')
time_beam2 = LpVariable("TimeBeam2", lowBound=0, cat='Continuous')

# Define the question as a maximum or minimum problem
problem = LpProblem("RadiationTreatment", LpMinimize)

# Define the objective function
objective = 0.3 * time_beam1 + 0.2 * time_beam2 + 0.6 * time_beam1 + 0.4 * time_beam2
problem += objective

# Define the constraints
problem += 0.2 * time_beam1 + 0.1 * time_beam2 <= 4
problem += 0.6 * time_beam1 + 0.4 * time_beam2 >= 3

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("Time for Beam 1:", value(time_beam1))
print("Time for Beam 2:", value(time_beam2))
print("Total radiation to the pancreas:", value(objective))
print("## end solving")