from pulp import *

# Define the decision variables
num_camels = LpVariable("NumCamels", lowBound=0, cat='Integer')
num_trucks = LpVariable("NumTrucks", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("DesertTransportation", LpMinimize)

# Define the objective function
# minimize the total hours required
objective = 12 * num_camels + 5 * num_trucks
problem += objective

# Define the constraints
# total goods to deliver
problem += 50 * num_camels + 150 * num_trucks >= 1500
# more camel caravans than desert trucks
problem += num_camels >= num_trucks

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of camel caravans:", num_camels.value())
print("The number of desert trucks:", num_trucks.value())
print("The total hours required:", objective.value())
print("## end solving")