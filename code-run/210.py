from pulp import *

# Define the decision variables
# number of premium printers
num_premium = LpVariable("NumPremium", lowBound=0, cat='Integer')
# number of regular printers
num_regular = LpVariable("NumRegular", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("OfficePrinterProblem", LpMinimize)

# Define the objective function
problem += num_premium + num_regular

# Define the constraints
problem += 30 * num_premium + 20 * num_regular >= 200
problem += 4 * num_premium + 3 * num_regular <= 35
problem += num_regular <= -1 + num_premium

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of premium printers:", num_premium.value())
print("The number of regular printers:", num_regular.value())
print("The total number of printers:", problem.objective.value())
print("## end solving")