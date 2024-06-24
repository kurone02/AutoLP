from pulp import *

# Define the decision variables
# number of acres of potatoes to plant
num_acres_potatoes = LpVariable("NumAcresPotatoes", lowBound=12, cat='Integer')
# number of acres of cucumbers to plant
num_acres_cucumbers = LpVariable("NumAcresCucumbers", lowBound=15, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("FarmerProfitProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 500 * num_acres_potatoes + 650 * num_acres_cucumbers
problem += objective

# Define the constraints
# minimum potatoes constraint
problem += num_acres_potatoes >= 12
# minimum cucumbers constraint
problem += num_acres_cucumbers >= 15
# total acres planted constraint
problem += num_acres_potatoes + num_acres_cucumbers <= 50
# cucumber preference constraint
problem += num_acres_cucumbers <= 2 * num_acres_potatoes

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("Acres of potatoes:", num_acres_potatoes.value())
print("Acres of cucumbers:", num_acres_cucumbers.value())
print("The maximum profit:", objective.value())
print("## end solving")