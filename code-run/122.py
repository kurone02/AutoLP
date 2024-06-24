from pulp import *

# Define the variables
num_high_intensity_drills = LpVariable("NumHighIntensityDrills", lowBound=0, cat='Integer')
num_low_intensity_drills = LpVariable("NumLowIntensityDrills", lowBound=10, cat='Integer')

# Define the problem
problem = LpProblem("GemFactoryProblem", LpMinimize)
objective = num_high_intensity_drills + num_low_intensity_drills
problem += objective

# Define the constraints
problem += 50 * num_high_intensity_drills + 30 * num_low_intensity_drills >= 800
problem += num_high_intensity_drills * 50 + num_low_intensity_drills * 20 <= 700
problem += num_high_intensity_drills <= 0.4 * (num_high_intensity_drills + num_low_intensity_drills)
problem += num_low_intensity_drills >= 10

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of high intensity drills:", value(num_high_intensity_drills))
print("The number of low intensity drills:", value(num_low_intensity_drills))
print("Total number of drills needed:", value(objective))
print("## end solving")