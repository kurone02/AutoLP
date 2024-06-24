from pulp import *

# Define the variables
num_dine_in = LpVariable("NumDineIn", lowBound=0, cat='Integer')
num_food_truck = LpVariable("NumFoodTruck", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("SandwichCompanyProblem", LpMinimize)
objective = num_dine_in + num_food_truck
problem += objective

# Define the constraints
problem += 100 * num_dine_in + 50 * num_food_truck >= 500
problem += 8 * num_dine_in + 3 * num_food_truck <= 35

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of dine-in stores:", value(num_dine_in))
print("The number of food trucks:", value(num_food_truck))
print("The total number of stores:", value(objective))
print("## end solving")