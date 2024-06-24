from pulp import *

# Define the variables
num_shirts = LpVariable("NumShirts", lowBound=0, cat='Integer')
num_shorts = LpVariable("NumShorts", lowBound=0, cat='Integer')
num_pants = LpVariable("NumPants", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("GandhiClothProblem", LpMaximize)
objective = (12 - 6) * num_shirts + (8 - 4) * num_shorts + (15 - 8) * num_pants
problem += objective

# Define the constraints
problem += 3 * num_shirts + 2 * num_shorts + 6 * num_pants <= 150
problem += 4 * num_shirts + 3 * num_shorts + 4 * num_pants <= 160

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of shirts produced each week:", value(num_shirts))
print("The number of shorts produced each week:", value(num_shorts))
print("The number of pants produced each week:", value(num_pants))
print("Shirt machinery rented:", 200 * value(num_shirts))
print("Shorts machinery rented:", 150 * value(num_shorts))
print("Pants machinery rented:", 100 * value(num_pants))
print("The maximum weekly profit:", value(objective))
print("## end solving")