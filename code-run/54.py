from pulp import *

# Define the variables
kg_syrup = LpVariable("KgSyrup", lowBound=3, upBound=10, cat='Continuous')
kg_candy = LpVariable("KgCandy", lowBound=5, upBound=12, cat='Continuous')

# Define the problem
problem = LpProblem("MapleFarmProblem", LpMaximize)
objective = 20 * kg_syrup + 15 * kg_candy
problem += objective

# Define the constraints
problem += 2 * kg_syrup + 2 * kg_candy <= 20
problem += kg_syrup >= 3
problem += kg_candy >= 5
problem += kg_syrup <= 10
problem += kg_candy <= 12

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of kg of maple syrup made:", value(kg_syrup))
print("The number of kg of maple candy made:", value(kg_candy))
print("The total profit:", value(objective))
print("## end solving")