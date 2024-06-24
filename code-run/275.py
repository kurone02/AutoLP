from pulp import *

# Define the decision variables
kg_mix1 = LpVariable("kg_mix1", lowBound=0, cat='Continuous')
kg_mix2 = LpVariable("kg_mix2", lowBound=0, cat='Continuous') 

# Define the question as a minimum or maximum problem
problem = LpProblem("SuperShopProfitProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 12 * kg_mix1 + 15 * kg_mix2
problem += objective

# Define the constraints
# total kg of cat paw snacks
problem += 0.20 * kg_mix1 + 0.35 * kg_mix2 <= 20
# total kg of gold shark snacks
problem += 0.80 * kg_mix1 + 0.65 * kg_mix2 <= 50

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The kg of the first mix:", kg_mix1.value())
print("The kg of the second mix:", kg_mix2.value())
print("The total profit:", objective.value())
print("## end solving")