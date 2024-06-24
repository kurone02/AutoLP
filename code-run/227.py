from pulp import *

# Define the decision variables
# number of camels
num_camels = LpVariable("NumCamels", lowBound=0, cat='Integer')
# number of horses
num_horses = LpVariable("NumHorses", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("AnimalTransportationProblem", LpMinimize)

# Define the objective function
# minimize the total number of animals
objective = num_camels + num_horses
problem += objective

# Define the constraints
# total packages constraint
problem += 50 * num_camels + 60 * num_horses >= 1000
# total food units constraint
problem += 20 * num_camels + 30 * num_horses <= 450
# horses cannot exceed camels constraint
problem += num_horses <= num_camels

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of camels:", num_camels.value())
print("The number of horses:", num_horses.value())
print("Total number of animals:", objective.value())
print("## end solving")