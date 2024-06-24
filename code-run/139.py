from pulp import *

# Define the decision variables
# number of nurses
num_nurses = LpVariable("NumNurses", lowBound=0, cat='Integer')
# number of pharmacists
num_pharmacists = LpVariable("NumPharmacists", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("ClinicSchedulingProblem", LpMinimize)

# Define the objective function
# minimize the total number of workers
objective = num_nurses + num_pharmacists
problem += objective

# Define the constraints
# total hours of healthcare labor
problem += 5 * num_nurses + 7 * num_pharmacists <= 200
# total salary
problem += 250 * num_nurses + 300 * num_pharmacists <= 9000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of nurses:", num_nurses.value())
print("The number of pharmacists:", num_pharmacists.value())
print("The total number of workers:", objective.value())
print("## end solving")