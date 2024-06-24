from pulp import *

# Define the decision variables
# number of ramen packs
num_ramen_packs = LpVariable("NumRamenPacks", lowBound=0, cat='Integer')
# number of fries packs
num_fries_packs = LpVariable("NumFriesPacks", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("SalesmanNutritionProblem", LpMinimize)

# Define the objective function
# minimize the total sodium intake
objective = 100 * num_ramen_packs + 75 * num_fries_packs
problem += objective

# Define the constraints
# total calories
problem += 400 * num_ramen_packs + 300 * num_fries_packs >= 3000
# total protein
problem += 20 * num_ramen_packs + 10 * num_fries_packs >= 80
# ramen packs constraint
problem += num_ramen_packs <= 0.3 * (num_ramen_packs + num_fries_packs)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of ramen packs:", num_ramen_packs.value())
print("The number of fries packs:", num_fries_packs.value())
print("The total sodium intake:", objective.value())
print("## end solving")