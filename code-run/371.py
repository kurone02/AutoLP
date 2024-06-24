from pulp import *

# Define the decision variables
invest_1 = LpVariable("Investment1", lowBound=0, cat='Continuous')
invest_2 = LpVariable("Investment2", lowBound=0, cat='Continuous')
invest_3 = LpVariable("Investment3", lowBound=0, cat='Continuous')
invest_4 = LpVariable("Investment4", lowBound=0, cat='Continuous')

# Define the problem
problem = LpProblem("StockcoInvestmentProblem", LpMaximize)

# Define the objective function
# maximize the total NPV
objective = 16000 * invest_1 + 22000 * invest_2 + 12000 * invest_3 + 8000 * invest_4
problem += objective

# Define the constraints
# total cash outflow
problem += 5000 * invest_1 + 7000 * invest_2 + 4000 * invest_3 + 3000 * invest_4 <= 14000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("Investment in 1:", invest_1.value())
print("Investment in 2:", invest_2.value())
print("Investment in 3:", invest_3.value())
print("Investment in 4:", invest_4.value())
print("Total NPV:", objective.value())
print("## end solving")