from pulp import *

# Define the decision variables
num_led = LpVariable("NumLED", lowBound=0, cat='Integer')
num_fluorescence = LpVariable("NumFluorescence", lowBound=0, cat='Integer')

# Define the question as a minimum or maximum problem
problem = LpProblem("LightingCompanyProblem", LpMinimize)

# Define the objective function
# minimize the total number of light changes
objective = 3 * num_led + 4 * num_fluorescence
problem += objective

# Define the constraints
# total number of lights
problem += num_led + num_fluorescence >= 300
# total electricity usage
problem += 5 * num_led + 8 * num_fluorescence <= 2000
# at least 30% of the installed lights must be fluorescence lamps
problem += num_fluorescence >= 0.3 * (num_led + num_fluorescence)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of LED lights:", num_led.value())
print("The number of fluorescence lamps:", num_fluorescence.value())
print("The total number of light changes:", objective.value())
print("## end solving")