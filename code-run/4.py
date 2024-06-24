from pulp import *

# Define the variables
num_klun_pills = LpVariable("NumKlunPills", lowBound=0, cat='Integer')
num_tao_pills = LpVariable("NumTaoPills", lowBound=0, cat='Integer') 

# Define the problem
problem = LpProblem("MedicinePurchaseProblem", LpMinimize)

# Define the objective function
objective = 2.6 * num_klun_pills + 3.2 * num_tao_pills
problem += objective

# Define the constraints
problem += 1.5 * num_klun_pills + 1.3 * num_tao_pills >= 6
problem += 1.8 * num_klun_pills + 2 * num_tao_pills >= 8

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of Klun pills:", num_klun_pills.value())
print("The number of Tao pills:", num_tao_pills.value())
print("The total cost is:", objective.value())
print("## end solving")