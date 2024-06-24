from pulp import *

# Define the decision variables
# number of acres of turnips to plant
num_acres_turnips = LpVariable("NumAcresTurnips", lowBound=0, cat='Integer')
# number of acres of pumpkins to plant
num_acres_pumpkins = LpVariable("NumAcresPumpkins", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("FarmerProfitProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 300 * num_acres_turnips + 450 * num_acres_pumpkins
problem += objective

# Define the constraints
# total acres available
problem += num_acres_turnips + num_acres_pumpkins <= 500
# total watering minutes available
problem += 50 * num_acres_turnips + 90 * num_acres_pumpkins <= 40000
# total pesticide available
problem += 80 * num_acres_turnips + 50 * num_acres_pumpkins <= 34000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("Acres of Turnips to grow:", num_acres_turnips.value())
print("Acres of Pumpkins to grow:", num_acres_pumpkins.value())
print("The maximum revenue that can be generated:", objective.value())
print("## end solving")