from pulp import *

# Define the variables
num_high_volume = LpVariable("NumHighVolume", lowBound=0, cat='Integer')
num_low_volume = LpVariable("NumLowVolume", lowBound=0, cat='Integer') 

# Define the problem
problem = LpProblem("OilGasCompanyProblem", LpMinimize)

# Define the objective function
problem += num_high_volume + num_low_volume

# Define the constraints
problem += 10000 * num_high_volume + 5000 * num_low_volume >= 150000
problem += 12 * num_high_volume + 5 * num_low_volume <= 160
problem  += num_high_volume <= 0.35*num_high_volume + 0.35*num_low_volume # problem += num_high_volume / (num_high_volume + num_low_volume) <= 0.35
problem += num_low_volume >= 8

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of high-volume pipes:", num_high_volume.value())
print("The number of low-volume pipes:", num_low_volume.value())
print("Total number of pipes:", (num_high_volume.value() + num_low_volume.value()))
print("## end solving")