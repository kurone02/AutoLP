from pulp import *

# Define the decision variables
# number of square feet planted with sunflowers
num_sqft_sunflowers = LpVariable("Sunflowers", lowBound=0, cat='Integer')
# number of square feet planted with roses
num_sqft_roses = LpVariable("Roses", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("GardenerProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 450 * num_sqft_sunflowers + 100 * num_sqft_roses
problem += objective

# Define the constraints
# total seed cost
problem += 67 * num_sqft_sunflowers + 52 * num_sqft_roses <= 6500
# total acres planted
problem += num_sqft_sunflowers + num_sqft_roses <= 100

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of square feet planted with sunflowers:", num_sqft_sunflowers.value())
print("The number of square feet planted with roses:", num_sqft_roses.value())
print("The total profit:", objective.value())
print("## end solving")