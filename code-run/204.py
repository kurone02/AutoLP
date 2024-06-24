from pulp import *

# Define the decision variables
# number of machines of type A
num_machines_A = LpVariable("NumMachinesA", lowBound=5, cat='Integer')
# number of machines of type B
num_machines_B = LpVariable("NumMachinesB", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("FactoryProblem", LpMinimize)

# Define the objective function
# minimize the total number of machines
objective = num_machines_A + num_machines_B
problem += objective

# Define the constraints
# total items produced
problem += 30 * num_machines_A + 50 * num_machines_B >= 1000
# total kWh consumed
problem += 100 * num_machines_A + 120 * num_machines_B <= 3000
# at most 30% of the machines must be of type B
problem += num_machines_B <= 0.3 * (num_machines_A + num_machines_B)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of machine A:", num_machines_A.value())
print("The number of machine B:", num_machines_B.value())
print("The minimum number of machines:", objective.value())
print("## end solving")