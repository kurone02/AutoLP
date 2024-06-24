from pulp import *

# Define the decision variables
# number of goat curry bowls
num_goat_curry = LpVariable("GoatCurry", lowBound=0, cat='Integer')
# number of chicken curry bowls
num_chicken_curry = LpVariable("ChickenCurry", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("CurryProblem", LpMinimize)

# Define the objective function
# minimize the total amount of curry base used
objective = 6 * num_goat_curry + 5 * num_chicken_curry
problem += objective

# Define the constraints
# at least 25% of the bowls must be chicken curry
problem += num_chicken_curry >= 0.25 * (num_goat_curry + num_chicken_curry)
# number of goat curry bowls must be larger than the number of chicken curry bowls
problem += num_goat_curry - num_chicken_curry >= 1
# total goat meat available
problem += 3 * num_goat_curry <= 1500
# total chicken meat available
problem += 5 * num_chicken_curry <= 2000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of goat curry bowls:", num_goat_curry.value())
print("The number of chicken curry bowls:", num_chicken_curry.value())
print("The total amount of curry base used:", objective.value())
print("## end solving")