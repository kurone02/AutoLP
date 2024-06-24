from pulp import *

# Define the decision variables
# number of personal licenses
num_personal_licenses = LpVariable("NumPersonalLicenses", lowBound=0, cat='Integer')
# number of commercial licenses
num_commercial_licenses = LpVariable("NumCommercialLicenses", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("PlatinumDatabaseProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 450 * num_personal_licenses + 1200 * num_commercial_licenses
problem += objective

# Define the constraints
# total cost
problem += 550 * num_personal_licenses + 2000 * num_commercial_licenses <= 400000
# total licenses
problem += num_personal_licenses + num_commercial_licenses <= 300

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of personal licenses:", num_personal_licenses.value())
print("The number of commercial licenses:", num_commercial_licenses.value())
print("Total profit:", objective.value())
print("## end solving")