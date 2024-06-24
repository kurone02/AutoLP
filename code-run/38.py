from pulp import *

# Define the decision variables
# number of acres of guavas to plant
num_acres_guavas = LpVariable("AcresGuavas", lowBound=20, cat='Continuous')
# number of acres of mangos to plant
num_acres_mangos = LpVariable("AcresMangos", lowBound=40, cat='Continuous') 

# Define the question as a minimum or maximum problem
problem = LpProblem("FarmerProfitProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 300 * num_acres_guavas + 500 * num_acres_mangos
problem += objective

# Define the constraints
# total acres planted
problem += num_acres_guavas + num_acres_mangos <= 100
# preference for mangos
problem += num_acres_mangos <= 2 * num_acres_guavas

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of acres of guavas to grow:", num_acres_guavas.value())
print("The number of acres of mangos to grow:", num_acres_mangos.value())
print("The maximum profit:", objective.value())
print("## end solving")