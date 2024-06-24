from pulp import *

# Define the decision variables
# number of regular mix boxes
regular_mix = LpVariable("RegularMix", lowBound=0, cat='Integer')
# number of deluxe mix boxes
deluxe_mix = LpVariable("DeluxeMix", lowBound=0, cat='Integer') 
# number of cashew boxes
cashews = LpVariable("Cashews", lowBound=0, cat='Integer')
# number of raisin boxes
raisins = LpVariable("Raisins", lowBound=0, cat='Integer')
# number of caramel boxes
caramels = LpVariable("Caramels", lowBound=0, cat='Integer')
# number of chocolate boxes
chocolates = LpVariable("Chocolates", lowBound=0, cat='Integer')

# Define the question as a minimum or maximum problem
problem = LpProblem("ChocolateProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 0.8 * regular_mix + 0.9 * deluxe_mix + 0.7 * cashews + 0.6 * raisins + 0.5 * caramels + 0.75 * chocolates
problem += objective

# Define the constraints
# total number of boxes produced per day
problem += regular_mix + deluxe_mix + cashews + raisins + caramels + chocolates <= 20 * (regular_mix + deluxe_mix + cashews + raisins + caramels + chocolates)
# at least 20 boxes of each type of product each day
problem += regular_mix >= 20
problem += deluxe_mix >= 20
problem += cashews >= 20
problem += raisins >= 20
problem += caramels >= 20
problem += chocolates >= 20
# ingredient capacity
problem += regular_mix + 0.5 * deluxe_mix + 1 * cashews <= 120
problem += 1 * raisins <= 200
problem += 1 * caramels <= 100
problem += regular_mix + 0.5 * deluxe_mix + 1 * chocolates <= 160

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of regular mix boxes:", regular_mix.value())
print("The number of deluxe mix boxes:", deluxe_mix.value())
print("The number of cashew boxes:", cashews.value())
print("The number of raisin boxes:", raisins.value())
print("The number of caramel boxes:", caramels.value())
print("The number of chocolate boxes:", chocolates.value())
print("The maximum profit:", objective.value())
print("## end solving")