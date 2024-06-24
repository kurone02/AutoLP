from pulp import *

# Define the decision variables
num_choco_batches = LpVariable("NumChocoBatches", lowBound=0, cat='Integer')
num_oat_batches = LpVariable("NumOatBatches", lowBound=0, cat='Integer') 

# Define the problem
problem = LpProblem("CookieProblem", LpMaximize)

# Define the objective function
problem += 12 * num_choco_batches + 15 * num_oat_batches

# Define the constraints
problem += 10 * num_choco_batches + 8 * num_oat_batches <= 1000
problem += 20 * num_choco_batches + 15 * num_oat_batches <= 1200
problem += 50 * num_choco_batches + 30 * num_oat_batches <= 3000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of batches of chocolate chip cookies:", num_choco_batches.value())
print("The number of batches of oatmeal cookies:", num_oat_batches.value())
print("Total profit:", value(problem.objective))
print("## end solving")