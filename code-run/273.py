from pulp import *

# Define the decision variables
# number of washing machines
num_washing_machines = LpVariable("NumWashingMachines", lowBound=0, cat='Integer')
# number of freezers
num_freezers = LpVariable("NumFreezers", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("ApplianceRepairProblem", LpMaximize)

# Define the objective function
# maximize the total earnings
objective = 250 * num_washing_machines + 375 * num_freezers
problem += objective

# Define the constraints
# total inspection time
problem += 30 * num_washing_machines + 20 * num_freezers <= 5000
# total fixing time
problem += 90 * num_washing_machines + 125 * num_freezers <= 20000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of washing machines:", num_washing_machines.value())
print("The number of freezers:", num_freezers.value())
print("Total earnings:", objective.value())
print("## end solving")