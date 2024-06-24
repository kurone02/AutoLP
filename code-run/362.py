from pulp import *

# Define the decision variables
amount_in_municipal_bonds = LpVariable("AmountInMunicipalBonds", lowBound=0, cat='Continuous')
amount_in_CDs = LpVariable("AmountInCDs", lowBound=0, cat='Continuous')
amount_in_t_bills = LpVariable("AmountInTBills", lowBound=0, cat='Continuous')
amount_in_growth_stocks = LpVariable("AmountInGrowthStocks", lowBound=0, cat='Continuous')

# Define the question as a minimum or maximum problem
problem = LpProblem("InvestmentProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 0.085 * amount_in_municipal_bonds + 0.05 * amount_in_CDs + 0.065 * amount_in_t_bills + 0.13 * amount_in_growth_stocks
problem += objective

# Define the constraints
# no more than 20% in municipal bonds
problem += amount_in_municipal_bonds <= 0.2 * 70000
# investment in CDs should not exceed the other three alternatives
problem += amount_in_CDs <= 0.7 * 70000
# at least 30% invested in t-bills and CDs
problem += amount_in_t_bills + 0.3 * 70000
# more should be invested in CDs and t-bills than in municipal bonds and growth stocks by a ratio of 1.2 to 1
problem += amount_in_CDs + 1.2 * amount_in_t_bills - 1.2 * amount_in_municipal_bonds - 1.2 * amount_in_growth_stocks >= 0
# all $70,000 should be invested
problem += amount_in_municipal_bonds + amount_in_CDs + amount_in_t_bills + amount_in_growth_stocks == 70000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("Amount to invest in Municipal Bonds:", amount_in_municipal_bonds.value())
print("Amount to invest in CDs:", amount_in_CDs.value())
print("Amount to invest in T-Bills:", amount_in_t_bills.value())
print("Amount to invest in Growth Stocks:", amount_in_growth_stocks.value())
print("Total Profit:", objective.value())
print("## end solving")