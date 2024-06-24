from pulp import *

# Define the decision variables
# number of acai berry smoothies
num_acai_smoothies = LpVariable("NumAcaiSmoothies", lowBound=0, cat='Integer')
# number of banana chocolate smoothies
num_chocolate_smoothies = LpVariable("NumChocolateSmoothies", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("SmoothieShopProblem", LpMinimize)

# Define the objective function
# minimize the total amount of water used
objective = 3 * num_acai_smoothies + 4 * num_chocolate_smoothies
problem += objective

# Define the constraints
# number of acai berry smoothies
problem += num_acai_smoothies <= num_chocolate_smoothies
# loyal customer base
problem += num_acai_smoothies >= 0.35 * (num_acai_smoothies + num_chocolate_smoothies)
# acai berries constraint
problem += num_acai_smoothies * 7 <= 3500
# banana chocolate constraint
problem += num_chocolate_smoothies * 6 <= 3200

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of acai berry smoothies:", num_acai_smoothies.value())
print("The number of banana chocolate smoothies:", num_chocolate_smoothies.value())
print("The total amount of water used:", objective.value())
print("## end solving")