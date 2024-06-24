from pulp import *

# Define the decision variables
# investment in younger sister's company
investment_younger_sister = LpVariable("InvestmentYoungerSister", lowBound=0, cat='Continuous')
# investment in elder sister's company
investment_elder_sister = LpVariable("InvestmentElderSister", lowBound=0, cat='Continuous') 

# Define the question as a minimum or maximum problem
problem = LpProblem("InvestmentProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 0.05 * investment_younger_sister + 0.08 * investment_elder_sister
problem += objective

# Define the constraints
# total investment
problem += investment_younger_sister + investment_elder_sister <= 5000
# minimum investment in younger sister's company
problem += investment_younger_sister >= 0.40 * (investment_younger_sister + investment_elder_sister)
# minimum investment in elder sister's company
problem += investment_elder_sister >= 2000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The amount to invest in the younger sister's company:", investment_younger_sister.value())
print("The amount to invest in the elder sister's company:", investment_elder_sister.value())
print("The maximum profit from the investment:", objective.value())
print("## end solving")