from pulp import *

# Define the decision variables
# number of acres processed by windrower
num_acres_windrower = LpVariable("AcresWindrower", lowBound=0, cat='Integer')
# number of acres processed by harvester
num_acres_harvester = LpVariable("AcresHarvester", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("FarmerProblem", LpMaximize)

# Define the objective function
# maximize the total amount of hay processed
objective = 10 * num_acres_windrower + 8 * num_acres_harvester
problem += objective

# Define the constraints
# total fuel
problem += 2 * num_acres_windrower + num_acres_harvester <= 300
# total methane gas
problem += 5 * num_acres_windrower + 3 * num_acres_harvester <= 800
# total acres processed
problem += num_acres_windrower + num_acres_harvester <= 200

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The acres processed by windrower:", num_acres_windrower.value())
print("The acres processed by harvester:", num_acres_harvester.value())
print("The amount of hay processed:", objective.value())
print("## end solving")