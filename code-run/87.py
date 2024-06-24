from pulp import *

# Define the decision variables
# money invested in the clothing company
money_clothing = LpVariable("MoneyClothing", lowBound=0, cat='Continuous')
# money invested in the tech company
money_tech = LpVariable("MoneyTech", lowBound=0, upBound=500, cat='Continuous') 

# Define the question as a minimum or maximum problem
problem = LpProblem("InvestmentProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 0.07 * money_clothing + 0.10 * money_tech
problem += objective

# Define the constraints
# total amount of money invested
problem += money_clothing + money_tech <= 3000
# money invested in the clothing company constraint
problem += money_clothing >= 4 * money_tech

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("Money invested in clothing company:", money_clothing.value())
print("Money invested in tech company:", money_tech.value())
print("Total profit:", objective.value())
print("## end solving")