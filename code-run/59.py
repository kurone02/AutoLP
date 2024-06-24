from pulp import *

# Define the decision variables
# number of hectares of carrots to plant
num_hectares_carrots = LpVariable("HectaresCarrots", lowBound=25, cat='Continuous')
# number of hectares of pumpkins to plant
num_hectares_pumpkins = LpVariable("HectaresPumpkins", lowBound=20, cat='Continuous') 

# Define the question as a minimum or maximum problem
problem = LpProblem("FarmerProfitProblem", LpMaximize)

# Define the objective function
# maximize the total profit from selling carrots and pumpkins
objective = 300 * num_hectares_carrots + 500 * num_hectares_pumpkins
problem += objective

# Define the constraints
# total acres planted
problem += num_hectares_carrots + num_hectares_pumpkins <= 200
# at least 25 hectares of carrots constraint
problem += num_hectares_carrots >= 25
# at least 20 hectares of pumpkins constraint
problem += num_hectares_pumpkins >= 20
# soil and weather condition constraint
problem += num_hectares_carrots <= 2 * num_hectares_pumpkins

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of hectares of carrots planted:", num_hectares_carrots.value())
print("The number of hectares of pumpkins planted:", num_hectares_pumpkins.value())
print("Total Profit:", objective.value())
print("## end solving")