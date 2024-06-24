from pulp import *

# Define the decision variables
# number of dollars invested in NFTs
num_nfts = LpVariable("NFTsInvestment", lowBound=0, cat='Continuous')
# number of dollars invested in cryptocurrency
num_crypto = LpVariable("CryptoInvestment", lowBound=0, cat='Continuous') 

# Define the question as a minimum or maximum problem
problem = LpProblem("LisaInvestmentProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 0.30 * num_nfts + 0.40 * num_crypto
problem += objective

# Define the constraints
# total investment
problem += num_nfts + num_crypto <= 5000
# minimum NFTs investment
problem += num_nfts >= 0.25 * (num_nfts + num_crypto)
# minimum crypto investment
problem += num_crypto >= 2300

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("Dollars invested in NFTs:", num_nfts.value())
print("Dollars invested in crypto-currency:", num_crypto.value())
print("Total profit:", objective.value())
print("## end solving")