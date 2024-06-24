from pulp import *

# Define the variables
num_calcium_pills = LpVariable("NumCalciumPills", lowBound=0, cat='Integer')
num_vitamin_D_pills = LpVariable("NumVitaminDPills", lowBound=40, cat='Integer')

# Define the problem
problem = LpProblem("MedicationProblem", LpMinimize)
objective = 5 * num_calcium_pills + 6 * num_vitamin_D_pills
problem += objective

# Define the constraints
problem += num_calcium_pills + num_vitamin_D_pills >= 130
problem += num_calcium_pills >= num_vitamin_D_pills

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of calcium pills:", num_calcium_pills.value())
print("The number of vitamin D pills:", num_vitamin_D_pills.value())
print("The total time for the medication to be effective:", objective.value())
print("## end solving")