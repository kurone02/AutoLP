from pulp import *

# Define the decision variables
oil_shares = LpVariable("OilShares", lowBound=0, cat='Integer')
auto_shares = LpVariable("AutoShares", lowBound=0, cat='Integer')
pharmaceutical_shares = LpVariable("PharmaceuticalShares", lowBound=0, cat='Integer')
oil = LpVariable("Oil", cat='Binary')
auto = LpVariable("Auto", cat='Binary')
pharmaceutical = LpVariable("Pharmaceutical", cat='Binary')

# Define the question as a maximum or minimum problem
problem = LpProblem("InvestmentProblem", LpMaximize)

# Define the objective function
objective = 11 * oil_shares + 4 * auto_shares + 2 * pharmaceutical_shares
problem += objective

# Define the constraints
problem += 120 * oil_shares + 52 * auto_shares + 18 * pharmaceutical_shares <= 100000
problem += 40000 <= 120 * oil_shares
problem += 40000 <= 52 * auto_shares
problem += 40000 <= 18 * pharmaceutical_shares
problem += oil + auto + pharmaceutical <= 3
problem += 10000 <= oil_shares * 120

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of oil stock shares:", oil_shares.value())
print("The number of auto stock shares:", auto_shares.value())
print("The number of pharmaceutical stock shares:", pharmaceutical_shares.value())
print("The maximum annual income:", objective.value())
print("## end solving")