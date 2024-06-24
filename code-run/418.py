from pulp import *

# Define the variables
x1 = LpVariable("MunicipalBonds", 0, 70000)
x2 = LpVariable("CDs", 0, 70000)
x3 = LpVariable("T-Bills", 0, 70000)
x4 = LpVariable("GrowthStocks", 0, 70000)

# Define the problem
prob = LpProblem("InvestmentProblem", LpMaximize)

# Define the objective function
prob += 0.085 * x1 + 0.05 * x2 + 0.065 * x3 + 0.13 * x4

# Define the constraints
prob += x1 <= 0.2 * 70000
prob += x2 <= 70000 - x1 - x3 - x4
prob += x3 + 0.3 * 70000 <= x2 + 0.3 * 70000
prob += 1.2 * x2 + 1.2 * x3 <= x1 + x4
prob += x1 + x2 + x3 + x4 == 70000

# Solve the problem
status = prob.solve()

# Output the answer
print("## start solving")
print("Amount to invest in Municipal Bonds:", value(x1))
print("Amount to invest in CDs:", value(x2))
print("Amount to invest in T-Bills:", value(x3))
print("Amount to invest in Growth Stocks:", value(x4))
print("Total Profit:", value(prob.objective))
print("## end solving")