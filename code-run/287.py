from pulp import *

# Define the decision variables
num_low_power = LpVariable("NumLowPower", lowBound=0, cat='Integer')
num_high_power = LpVariable("NumHighPower", lowBound=0, cat='Integer')

# Define the question as a minimum or maximum problem
problem = LpProblem("AirConditionerPurchase", LpMinimize)

# Define the objective function
problem += num_low_power + num_high_power

# Define the constraints
problem += 12 * num_low_power >= 250
problem += 17 * num_high_power >= 250
problem += 150 * num_low_power <= 8000
problem += 250 * num_high_power <= 8000
problem += num_low_power <= 0.3 * (num_low_power + num_high_power)
problem += num_high_power >= 7

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of low power air conditioners:", num_low_power.value())
print("The number of high power air conditioners:", num_high_power.value())
print("The total number of air conditioners:", (num_low_power + num_high_power).value())
print("## end solving")