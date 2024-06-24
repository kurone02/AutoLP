from pulp import *

# Define the decision variables
# number of oil stock shares
num_oil_shares = LpVariable("NumOilShares", lowBound=0, cat='Integer')
# number of auto stock shares
num_auto_shares = LpVariable("NumAutoShares", lowBound=0, cat='Integer')
# number of pharmaceutical stock shares
num_pharmaceutical_shares = LpVariable("NumPharmaceuticalShares", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("StockInvestmentProblem", LpMaximize)

# Define the objective function
# maximize the total annual income
objective = 11 * num_oil_shares + 4 * num_auto_shares + 2 * num_pharmaceutical_shares
problem += objective

# Define the constraints
# total investment
problem += 120 * num_oil_shares + 52 * num_auto_shares + 18 * num_pharmaceutical_shares <= 100000
# maximum investment in any one stock
problem += 120 * num_oil_shares + 52 * num_auto_shares + 18 * num_pharmaceutical_shares <= 0.4 * 100000
# minimum investment in oil stock
problem += 120 * num_oil_shares >= 10000
# the broker has identified three stocks for investment
problem += num_oil_shares + num_auto_shares + num_pharmaceutical_shares <= 3

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of oil stock shares:", num_oil_shares.value())
print("The number of auto stock shares:", num_auto_shares.value())
print("The number of pharmaceutical stock shares:", num_pharmaceutical_shares.value())
print("The maximum annual income:", objective.value())
print("## end solving")