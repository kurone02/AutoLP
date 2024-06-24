from pulp import *

# Define the decision variables
# The amount of fertilizer C in kgs
kg_C = LpVariable("KgC", lowBound=0, cat='Continuous')
# The amount of fertilizer Y in kgs
kg_Y = LpVariable("KgY", lowBound=0, cat='Continuous') 

# Define the question as a minimum or maximum problem
problem = LpProblem("FertilizerProblem", LpMinimize)

# Define the objective function
# Minimize the total cost
objective = 2 * kg_C + 3 * kg_Y
problem += objective

# Define the constraints
# The amount of nitrous oxide
problem += 1.5 * kg_C + 5 * kg_Y >= 5
# The amount of vitamin mix
problem += 3 * kg_C + kg_Y >= 8
# The amount of fertilizer C and Y
problem += kg_C + kg_Y >= 0

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The amount of fertilizer C in kgs:", value(kg_C))
print("The amount of fertilizer Y in kgs:", value(kg_Y))
print("The minimum cost of the compound:", value(objective))
print("## end solving")