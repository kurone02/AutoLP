from pulp import *

# Define the decision variables
# number of bracelets
num_bracelets = LpVariable("NumBracelets", lowBound=0, cat='Integer')
# number of rings
num_rings = LpVariable("NumRings", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("JewelryCompanyProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 700 * num_bracelets + 300 * num_rings
problem += objective

# Define the constraints
# bracelets per day
problem += num_bracelets <= 4
# rings per day
problem += num_rings <= 7
# total jewels to check per day
problem += num_bracelets + num_rings <= 30

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of bracelets to make:", num_bracelets.value())
print("The number of rings to make:", num_rings.value())
print("The maximum profit:", objective.value())
print("## end solving")