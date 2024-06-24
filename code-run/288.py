from pulp import *

# Define the variables
num_bananas = LpVariable("NumBananas", lowBound=0, cat='Integer')
num_mangoes = LpVariable("NumMangoes", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("GorillaFruitConsumption", LpMinimize)
objective = 10 * num_bananas + 8 * num_mangoes
problem += objective

# Define the constraints
problem += 80 * num_bananas + 100 * num_mangoes >= 4000
problem += 20 * num_bananas + 15 * num_mangoes >= 150
problem += num_mangoes <= 0.33 * (num_bananas + num_mangoes)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of bananas:", value(num_bananas))
print("The number of mangoes:", value(num_mangoes))
print("The total sugar intake:", value(objective))
print("## end solving")