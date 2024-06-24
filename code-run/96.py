from pulp import *

# Define the decision variables
num_banana_haters_packages = LpVariable("NumBananaHatersPackages", lowBound=0, cat='Integer')
num_combo_packages = LpVariable("NumComboPackages", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("GroceryStoreProblem", LpMaximize)

# Define the objective function
problem += 6 * num_banana_haters_packages + 7 * num_combo_packages

# Define the constraints
problem += 6 * num_banana_haters_packages + 5 * num_combo_packages <= 10
problem += 30 * num_banana_haters_packages + 6 * num_combo_packages <= 20
problem += 30 * num_banana_haters_packages + 20 * num_combo_packages <= 80

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of banana-haters packages:", num_banana_haters_packages.value())
print("The number of combo packages:", num_combo_packages.value())
print("The maximum net profit:", value(problem.objective))
print("## end solving")