from pulp import *

# Define the decision variables
# number of Meaties packages to produce
num_meaties = LpVariable("Meaties", lowBound=0, cat='Integer')
# number of Yummies packages to produce
num_yummies = LpVariable("Yummies", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("HealthyPetFoodProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = (2.80 - 0.25) * num_meaties + (2.00 - 0.20) * num_yummies
problem += objective

# Define the constraints
# total cereal
problem += 2 * num_meaties + 3 * num_yummies <= 400000
# total meat
problem += 3 * num_meaties + 1.5 * num_yummies <= 300000
# machine capacity for Meaties
problem += num_meaties <= 90000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of Meaties packages to produce:", num_meaties.value())
print("The number of Yummies packages to produce:", num_yummies.value())
print("The maximum profit:", objective.value())
print("## end solving")