from pulp import *

# Define the variables
invest_1 = LpVariable("Invest1", lowBound=0, cat='Continuous')
invest_2 = LpVariable("Invest2", lowBound=0, cat='Continuous')
invest_3 = LpVariable("Invest3", lowBound=0, cat='Continuous')
invest_4 = LpVariable("Invest4", lowBound=0, cat='Continuous')

# Define the problem
problem = LpProblem("StockcoInvestment", LpMaximize)

# Define the objective function
problem += invest_1 + invest_2 + invest_3 + invest_4

# Define the constraints
problem += invest_1 + invest_2 + invest_3 + invest_4 <= 14000
problem += invest_1 >= 5000
problem += invest_2 >= 7000
problem += invest_3 >= 4000
problem += invest_4 >= 3000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("Investment in 1:", invest_1.value())
print("Investment in 2:", invest_2.value())
print("Investment in 3:", invest_3.value())
print("Investment in 4:", invest_4.value())
print("Total NPV:", value(problem.objective))
print("## end solving")