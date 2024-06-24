from pulp import *

# Define the decision variables
# number of acres of corn to plant
num_acres_corn = LpVariable("AcresCorn", lowBound=0, cat='Integer')
# number of acres of soybeans to plant
num_acres_soybeans = LpVariable("AcresSoybeans", lowBound=0, cat='Integer') 
# number of acres of wheat to plant
num_acres_wheat = LpVariable("AcresWheat", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("FarmerProfitProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 300 * num_acres_corn + 200 * num_acres_soybeans + 80 * num_acres_wheat
problem += objective

# Define the constraints
# total water required
problem += 200 * num_acres_corn + 150 * num_acres_soybeans + 125 * num_acres_wheat <= 35000
# total labor required
problem += 35 * num_acres_corn + 40 * num_acres_soybeans + 30 * num_acres_wheat <= 8000
# total acres planted
problem += num_acres_corn + num_acres_soybeans + num_acres_wheat <= 200

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("Acres of Corn to plant:", num_acres_corn.value())
print("Acres of Soybeans to plant:", num_acres_soybeans.value())
print("Acres of Wheat to plant:", num_acres_wheat.value())
print("Maximum Profit:", objective.value())
print("## end solving")