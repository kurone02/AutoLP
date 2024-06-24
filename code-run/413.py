from pulp import *

# Define the decision variables
# number of apple butter batches
num_apple_butter_batches = LpVariable("NumAppleButterBatches", lowBound=0, cat='Integer')
# number of apple sauce batches
num_apple_sauce_batches = LpVariable("NumAppleSauceBatches", lowBound=0, cat='Integer')
# number of apple jelly batches
num_apple_jelly_batches = LpVariable("NumAppleJellyBatches", lowBound=0, cat='Integer')

# Define the question as a minimum or maximum problem
problem = LpProblem("FriendlyFarmProfitMaximization", LpMaximize)

# Define the objective function
# maximize the total revenue
objective = 190 * num_apple_butter_batches + 170 * num_apple_sauce_batches + 155 * num_apple_jelly_batches
problem += objective

# Define the constraints
# total cooking time
problem += 3.5 * num_apple_butter_batches + 5.2 * num_apple_sauce_batches + 2.8 * num_apple_jelly_batches <= 500
# total labor time
problem += 1.2 * num_apple_butter_batches + 0.8 * num_apple_sauce_batches + 1.5 * num_apple_jelly_batches <= 240
# total apples used
problem += 40 * num_apple_butter_batches + 55 * num_apple_sauce_batches + 20 * num_apple_jelly_batches <= 6500

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("Number of Apple Butter batches to produce:", num_apple_butter_batches.value())
print("Number of Apple Sauce batches to produce:", num_apple_sauce_batches.value())
print("Number of Apple Jelly batches to produce:", num_apple_jelly_batches.value())
print("Total Revenue:", objective.value())
print("## end solving")