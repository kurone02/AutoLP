from pulp import *

# Define the decision variables
# number of apple smoothies
num_apple_smoothies = LpVariable("NumAppleSmoothies", lowBound=0, cat='Integer')
# number of orange smoothies
num_orange_smoothies = LpVariable("NumOrangeSmoothies", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("FoodTruckProblem", LpMaximize)

# Define the objective function
# maximize the total profit from selling smoothies
objective = 3.5 * num_apple_smoothies + 4.5 * num_orange_smoothies
problem += objective

# Define the constraints
# total cutting and blending time
problem += 6 * num_apple_smoothies + 5 * num_orange_smoothies <= 500
# total blending time
problem += 3 * num_apple_smoothies + 2 * num_orange_smoothies <= 500

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of apple smoothies:", num_apple_smoothies.value())
print("The number of orange smoothies:", num_orange_smoothies.value())
print("Total profit:", objective.value())
print("## end solving")