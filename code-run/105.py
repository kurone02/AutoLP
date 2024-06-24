from pulp import *

# Define the variables
kg_regular_mix = LpVariable("KgRegularMix", lowBound=0, cat='Continuous')
kg_sour_surprise_mix = LpVariable("KgSourSurpriseMix", lowBound=0, cat='Continuous')

# Define the problem
problem = LpProblem("CandyStoreProblem", LpMaximize)
objective = 3 * kg_regular_mix + 5 * kg_sour_surprise_mix
problem += objective

# Define the constraints
problem += 0.8 * kg_regular_mix + 0.1 * kg_sour_surprise_mix <= 80
problem += 0.2 * kg_regular_mix + 0.9 * kg_sour_surprise_mix <= 60

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The amount of regular mix:", value(kg_regular_mix))
print("The amount of sour surprise mix:", value(kg_sour_surprise_mix))
print("The profit:", value(objective))
print("## end solving")