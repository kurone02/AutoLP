from pulp import *

# Define the decision variables
# amount to invest in Municipal Bonds
amt_municipal_bonds = LpVariable("AmtMunicipalBonds", lowBound=0, cat='Continuous')
# amount to invest in CDs
amt_cds = LpVariable("AmtCDs", lowBound=0, cat='Continuous')
# amount to invest in T-Bills
amt_t_bills = LpVariable("AmtTBills", lowBound=0, cat='Continuous')
# amount to invest in Growth Stocks
amt_growth_stocks = LpVariable("AmtGrowthStocks", lowBound=0, cat='Continuous')

# Define the question as a minimum or maximum problem
problem = LpProblem("InvestmentProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 0.085 * amt_municipal_bonds + 0.05 * amt_cds + 0.065 * amt_t_bills + 0.13 * amt_growth_stocks
problem += objective

# Define the constraints
# maximum investment in Municipal Bonds
problem += amt_municipal_bonds <= 0.2 * 70000
# maximum investment in CDs
problem += amt_cds <= 70000 - amt_municipal_bonds - amt_t_bills - amt_growth_stocks
# minimum investment in T-Bills and CDs
problem += amt_t_bills + amt_cds >= 0.3 * 70000
# investment in CDs and T-Bills should be at least 1.2 times the investment in Municipal Bonds and Growth Stocks
problem += amt_cds + amt_t_bills - (amt_municipal_bonds + amt_growth_stocks) >= 0.2 * 70000
# total investment
problem += amt_municipal_bonds + amt_cds + amt_t_bills + amt_growth_stocks <= 70000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("Amount to invest in Municipal Bonds:", amt_municipal_bonds.value())
print("Amount to invest in CDs:", amt_cds.value())
print("Amount to invest in T-Bills:", amt_t_bills.value())
print("Amount to invest in Growth Stocks:", amt_growth_stocks.value())
print("Total Profit:", objective.value())
print("## end solving")