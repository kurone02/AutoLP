from pulp import *

# Define the decision variables
num_shirts = LpVariable("NumShirts", lowBound=0, cat='Integer')
num_shorts = LpVariable("NumShorts", lowBound=0, cat='Integer')
num_pants = LpVariable("NumPants", lowBound=0, cat='Integer')
rent_shirt_machinery = LpVariable("RentShirtMachinery", lowBound=0, cat='Integer')
rent_shorts_machinery = LpVariable("RentShortsMachinery", lowBound=0, cat='Integer')
rent_pants_machinery = LpVariable("RentPantsMachinery", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("GandhiProfitMaximization", LpMaximize)

# Define the objective function
objective = 12 * num_shirts + 6 * num_shorts + 8 * num_pants - (200 * rent_shirt_machinery + 150 * rent_shorts_machinery + 100 * rent_pants_machinery)
problem += objective

# Define the constraints
problem += 3 * num_shirts + 2 * num_shorts + 6 * num_pants <= 150
problem += 4 * num_shirts + 3 * num_shorts + 4 * num_pants <= 160
problem += rent_shirt_machinery >= num_shirts
problem += rent_shorts_machinery >= num_shorts
problem += rent_pants_machinery >= num_pants

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of shirts produced each week:", num_shirts.value())
print("The number of shorts produced each week:", num_shorts.value())
print("The number of pants produced each week:", num_pants.value())
print("Shirt machinery rented:", rent_shirt_machinery.value())
print("Shorts machinery rented:", rent_shorts_machinery.value())
print("Pants machinery rented:", rent_pants_machinery.value())
print("The maximum weekly profit:", objective.value())
print("## end solving")