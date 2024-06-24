from pulp import *

# Define the decision variables
# number of shirts produced each week
num_shirts = LpVariable("NumShirts", lowBound=0, cat='Integer')
# number of shorts produced each week
num_shorts = LpVariable("NumShorts", lowBound=0, cat='Integer')
# number of pants produced each week
num_pants = LpVariable("NumPants", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("GandhiClothProblem", LpMaximize)

# Define the objective function
# maximize weekly profits
objective = 12 * num_shirts + 6 * num_shorts + 8 * num_pants - (200 * num_shirts + 150 * num_shorts + 100 * num_pants)
problem += objective

# Define the constraints
# total hours of labor
problem += 3 * num_shirts + 2 * num_shorts + 6 * num_pants <= 150
# total sq yd of cloth
problem += 4 * num_shirts + 3 * num_shorts + 4 * num_pants <= 160
# non-negative production
problem += num_shirts >= 0
problem += num_shorts >= 0
problem += num_pants >= 0

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of shirts produced each week:", num_shirts.value())
print("The number of shorts produced each week:", num_shorts.value())
print("The number of pants produced each week:", num_pants.value())
print("Shirt machinery rented:", 200 * num_shirts.value())
print("Shorts machinery rented:", 150 * num_shorts.value())
print("Pants machinery rented:", 100 * num_pants.value())
print("The maximum weekly profit:", objective.value())
print("## end solving")