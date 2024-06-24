from pulp import *

# Define the decision variables
# number of phones
num_phones = LpVariable("NumPhones", lowBound=0, cat='Integer')
# number of laptops
num_laptops = LpVariable("NumLaptops", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("ElectronicsStoreProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 120 * num_phones + 40 * num_laptops
problem += objective

# Define the constraints
# total floor space
problem += 1 * num_phones + 4 * num_laptops <= 400
# 80% of all appliances in stock be laptops
problem += num_laptops >= 0.8 * (num_phones + num_laptops)
# total cost
problem += 400 * num_phones + 100 * num_laptops <= 6000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of phones:", num_phones.value())
print("The number of laptops:", num_laptops.value())
print("Total profit:", objective.value())
print("## end solving")