from pulp import *

# Define the decision variables
# number of investment 1
num_investment_1 = LpVariable("Investment1", lowBound=0, cat='Integer')
# number of investment 2
num_investment_2 = LpVariable("Investment2", lowBound=0, cat='Integer')
# number of investment 3
num_investment_3 = LpVariable("Investment3", lowBound=0, cat='Integer')
# number of investment 4
num_investment_4 = LpVariable("Investment4", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("StockcoInvestmentProblem", LpMaximize)

# Define the objective function
# maximize the total NPV
objective = 16000 * num_investment_1 + 22000 * num_investment_2 + 12000 * num_investment_3 + 8000 * num_investment_4
problem += objective

# Define the constraints
# total cash outflow constraint
problem += 5000 * num_investment_1 + 7000 * num_investment_2 + 4000 * num_investment_3 + 3000 * num_investment_4 <= 14000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("Investment in 1:", num_investment_1.value())
print("Investment in 2:", num_investment_2.value())
print("Investment in 3:", num_investment_3.value())
print("Investment in 4:", num_investment_4.value())
print("Total NPV:", objective.value())
print("## end solving")