from pulp import *

# Define the decision variables
num_acres_corn = LpVariable("NumAcresCorn", lowBound=0, cat='Integer')
num_acres_soybeans = LpVariable("NumAcresSoybeans", lowBound=0, cat='Integer')
num_acres_wheat = LpVariable("NumAcresWheat", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("FarmProfitMaximization", LpMaximize)

# Define the objective function
problem += 1.00 * 300 * num_acres_corn + 1.60 * 200 * num_acres_soybeans + 3.00 * 80 * num_acres_wheat

# Define the constraints
problem += num_acres_corn + num_acres_soybeans + num_acres_wheat <= 200
problem += 200 * num_acres_corn + 150 * num_acres_soybeans + 125 * num_acres_wheat <= 35000
problem += 35 * num_acres_corn + 40 * num_acres_soybeans + 30 * num_acres_wheat <= 8000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("Acres of Corn to plant:", value(num_acres_corn))
print("Acres of Soybeans to plant:", value(num_acres_soybeans))
print("Acres of Wheat to plant:", value(num_acres_wheat))
print("Maximum Profit:", value(problem.objective))
print("## end solving")