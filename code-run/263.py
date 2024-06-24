from pulp import *

# Define the decision variables
num_noodles = LpVariable("NumNoodles", lowBound=0, cat='Integer')
num_protein_bar = LpVariable("NumProteinBar", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("BobDietProblem", LpMinimize)
objective = 5 * num_noodles + 2.5 * num_protein_bar
problem += objective

# Define the constraints
problem += 600 * num_noodles + 250 * num_protein_bar >= 2000
problem += 1.5 * num_noodles + 5 * num_protein_bar >= 16

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of noodles servings:", num_noodles.value())
print("The number of protein bar servings:", num_protein_bar.value())
print("The cost of the diet:", objective.value())
print("## end solving")