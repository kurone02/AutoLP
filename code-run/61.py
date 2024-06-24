from pulp import *

# Define the decision variables
# number of acres of daikons to plant
num_acres_daikons = LpVariable("AcresDaikons", lowBound=0, cat='Integer')
# number of acres of fennels to plant
num_acres_fennels = LpVariable("AcresFennels", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("FarmerProfitProblem", LpMaximize)

# Define the objective function
# maximize the total revenue
objective = 300 * num_acres_daikons + 250 * num_acres_fennels
problem += objective

# Define the constraints
# total hours of watering
problem += 0.5 * num_acres_daikons + 1.5 * num_acres_fennels <= 500
# total compost
problem += 70 * num_acres_daikons + 50 * num_acres_fennels <= 7400
# total acres planted
problem += num_acres_daikons + num_acres_fennels <= 300

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("Number of acres to grow daikons:", num_acres_daikons.value())
print("Number of acres to grow fennels:", num_acres_fennels.value())
print("Total revenue:", objective.value())
print("## end solving")