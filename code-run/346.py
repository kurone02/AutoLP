from pulp import *

# Define the decision variables
# number of argon gas approaches to use
num_argon = LpVariable("NumArgon", lowBound=0, cat='Integer')
# number of halogen gas approaches to use
num_halogen = LpVariable("NumHalogen", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("BulbManufacturingProblem", LpMaximize)

# Define the objective function
# maximize the total number of light bulbs produced
objective = 2 * num_argon + 3 * num_halogen
problem += objective

# Define the constraints
# total gas available
problem += 10 * num_argon + 12 * num_halogen <= 150
# total glass available
problem += 12 * num_argon + 8 * num_halogen <= 120
# total heat generated
problem += 3 * num_argon + 4 * num_halogen <= 28

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of argon methods:", num_argon.value())
print("The number of halogen methods:", num_halogen.value())
print("The total number of light bulbs produced:", objective.value())
print("## end solving")