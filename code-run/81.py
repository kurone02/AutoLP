from pulp import *

# Define the variables
num_senior = LpVariable("NumSenior", lowBound=5, cat='Integer')
num_junior = LpVariable("NumJunior", lowBound=0, cat='Integer') 

# Define the problem
problem = LpProblem("AccountingFirmProblem", LpMinimize)

# Define the objective function
objective = 3000 * num_senior + 1000 * num_junior
problem += objective

# Define the constraints
problem += num_senior + num_junior >= 100
problem  += 3*num_senior >= num_junior # problem += num_senior >= num_junior / 3
problem += 3000 * num_senior + 1000 * num_junior <= 150000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of senior accountants:", num_senior.value())
print("The number of junior accountants:", num_junior.value())
print("Total wage bill:", objective.value())
print("## end solving")