from pulp import *

# Define the decision variables
num_A_to_I = LpVariable("NumAtoI", lowBound=0, cat='Integer')
num_A_to_II = LpVariable("NumAtoII", lowBound=0, cat='Integer')
num_B_to_I = LpVariable("NumBtoI", lowBound=0, cat='Integer')
num_B_to_II = LpVariable("NumBtoII", lowBound=0, cat='Integer')

# Define the question as a minimum or maximum problem
problem = LpProblem("FirefightingEquipmentProblem", LpMinimize)

# Define the objective function
objective = 8 * num_A_to_I + 12 * num_A_to_II + 16 * num_B_to_I + 4 * num_B_to_II
problem += objective

# Define the constraints
problem += num_A_to_I + num_A_to_II <= 800
problem += num_B_to_I + num_B_to_II <= 1000
problem += num_A_to_I + num_B_to_I >= 900
problem += num_A_to_II + num_B_to_II >= 600

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of alarm valves from Plant A to Center I:", num_A_to_I.value())
print("The number of alarm valves from Plant A to Center II:", num_A_to_II.value())
print("The number of alarm valves from Plant B to Center I:", num_B_to_I.value())
print("The number of alarm valves from Plant B to Center II:", num_B_to_II.value())
print("The minimum transportation cost:", objective.value())
print("## end solving")