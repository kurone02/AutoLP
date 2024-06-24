from pulp import *

# Define the decision variables
# number of premium desktops
num_premium = LpVariable("PremiumDesktops", lowBound=0, cat='Integer')
# number of regular desktops
num_regular = LpVariable("RegularDesktops", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("ElectronicsStoreProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 500 * num_premium + 300 * num_regular
problem += objective

# Define the constraints
# total cost of making desktops
problem += 2000 * num_premium + 1000 * num_regular <= 300000
# total desktops sold
problem += num_premium + num_regular <= 200

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of premium desktops:", num_premium.value())
print("The number of regular desktops:", num_regular.value())
print("The total profit:", objective.value())
print("## end solving")