from pulp import *

# Define the variables
# money invested in apartments
money_apartments = LpVariable("MoneyApartments", lowBound=0, cat='Continuous')
# money invested in townhouses
money_townhouses = LpVariable("MoneyTownhouses", lowBound=0, cat='Continuous') 

# Define the question as a minimum or maximum problem
problem = LpProblem("RealStateInvestmentProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 0.1 * money_apartments + 0.15 * money_townhouses
problem += objective

# Define the constraints
# money in apartments constraint
problem += money_apartments <= 200000
# total money invested constraint
problem += money_apartments + money_townhouses <= 600000
# money in apartments constraint
problem += money_apartments >= 0.5 * money_townhouses

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The money invested in apartments:", money_apartments.value())
print("The money invested in townhouses:", money_townhouses.value())
print("The maximum profit:", objective.value())
print("## end solving")