from pulp import *

# Define the decision variables
# number of acres of peaches to plant
num_acres_peaches = LpVariable("AcresPeaches", lowBound=0, cat='Integer')
# number of acres of nectarines to plant
num_acres_nectarines = LpVariable("AcresNectarines", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("FarmerProfitProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 200 * num_acres_peaches + 175 * num_acres_nectarines
problem += objective

# Define the constraints
# total acres available
problem += num_acres_peaches + num_acres_nectarines <= 80
# total planting hours
problem += 3 * num_acres_peaches + 4.5 * num_acres_nectarines <= 300
# total watering hours
problem += 2 * num_acres_peaches + 3 * num_acres_nectarines <= 250

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("Number of acres for peaches:", num_acres_peaches.value())
print("Number of acres for nectarines:", num_acres_nectarines.value())
print("Total profit:", objective.value())
print("## end solving")