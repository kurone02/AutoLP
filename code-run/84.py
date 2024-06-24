from pulp import *

# Define the decision variables
# amount invested in telecom
amount_telecom = LpVariable("AmountTelecom", lowBound=0, cat='Continuous')
# amount invested in healthcare
amount_healthcare = LpVariable("AmountHealthcare", lowBound=0, cat='Continuous') 

# Define the question as a minimum or maximum problem
problem = LpProblem("RobertsInvestmentProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 0.03 * amount_telecom + 0.01 * amount_healthcare
problem += objective

# Define the constraints
# total investment
problem += amount_telecom + amount_healthcare <= 100000
# maximum amount invested in telecom
problem += amount_telecom <= 70000
# minimum amount invested in telecom
problem += 3 * amount_healthcare <= amount_telecom

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("Amount invested in telecom:", value(amount_telecom))
print("Amount invested in healthcare:", value(amount_healthcare))
print("Total profit:", value(objective))
print("## end solving")