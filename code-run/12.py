from pulp import *

# Define the decision variables
# amount of pork in kg
kg_pork = LpVariable("kg_pork", lowBound=0, cat='Continuous')
# amount of chicken in kg
kg_chicken = LpVariable("kg_chicken", lowBound=0, cat='Continuous') 

# Define the question as a minimum or maximum problem
problem = LpProblem("MinCostProblem", LpMinimize)

# Define the objective function
# minimize the total cost of the mixture
objective = 40 * kg_pork + 50 * kg_chicken
problem += objective

# Define the constraints
# protein constraint
problem += 2 * kg_pork + 3 * kg_chicken >= 10
# fat constraint
problem += 4 * kg_pork + 2 * kg_chicken >= 15

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The amount of pork in kg:", kg_pork.value())
print("The amount of chicken in kg:", kg_chicken.value())
print("The minimum cost of the mixture:", objective.value())
print("## end solving")