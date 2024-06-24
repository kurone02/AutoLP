from pulp import *

# Define the decision variables
# number of acres of corn to plant
num_acres_corn = LpVariable("NumAcresCorn", lowBound=0, cat='Integer')
# number of acres of soybeans to plant
num_acres_soybeans = LpVariable("NumAcresSoybeans", lowBound=0, cat='Integer')
# number of acres of wheat to plant
num_acres_wheat = LpVariable("NumAcresWheat", lowBound=0, cat='Integer')

# Define the question as a minimum or maximum problem
problem = LpProblem("FarmerProfitProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 1 * num_acres_corn * 300 + 1.6 * num_acres_soybeans * 200 + 3 * num_acres_wheat * 80
problem += objective

# Define the constraints
# total water available
problem += 200 * num_acres_corn + 150 * num_acres_soybeans + 125 * num_acres_wheat <= 35000
# total labor hours available
problem += 35 * num_acres_corn + 40 * num_acres_soybeans + 30 * num_acres_wheat <= 8000
# total acres planted
problem += num_acres_corn + num_acres_soybeans + num_acres_wheat <= 200

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("Acres of corn to plant:", num_acres_corn.value())
print("Acres of soybeans to plant:", num_acres_soybeans.value())
print("Acres of wheat to plant:", num_acres_wheat.value())
print("Maximum Profit:", objective.value())
print("## end solving")