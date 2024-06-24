from pulp import *

# Define the decision variables
# number of acres of blueberries to plant
num_blueberry_acres = LpVariable("AcresBlueberry", lowBound=0, cat='Integer')
# number of acres of raspberries to plant
num_raspberry_acres = LpVariable("AcresRaspberry", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("FarmerProfitProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 56 * num_blueberry_acres + 75 * num_raspberry_acres
problem += objective

# Define the constraints
# total labor
problem += 6 * num_blueberry_acres + 3 * num_raspberry_acres <= 575
# total watering costs
problem += 22 * num_blueberry_acres + 25 * num_raspberry_acres <= 10000
# total acres planted
problem += num_blueberry_acres + num_raspberry_acres <= 300

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of blueberry acres:", num_blueberry_acres.value())
print("The number of raspberry acres:", num_raspberry_acres.value())
print("The total profit:", objective.value())
print("## end solving")