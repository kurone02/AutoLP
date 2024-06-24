from pulp import *

# Define the decision variables
# number of salinity tests
num_salinity_tests = LpVariable("NumSalinityTests", lowBound=0, cat='Integer')
# number of pH tests
num_ph_tests = LpVariable("NumPHTests", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("ChemicalCompanyProblem", LpMinimize)

# Define the objective function
# minimize the total number of probes used
objective = 3 * num_salinity_tests + 2 * num_ph_tests
problem += objective

# Define the constraints
# at least 250 pH tests
problem += num_ph_tests >= 250
# at least 400 tests
problem += num_salinity_tests + num_ph_tests >= 400
# at most 1.5 times more pH tests than salinity tests
problem += num_ph_tests <= 1.5 * num_salinity_tests

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of salinity tests:", num_salinity_tests.value())
print("The number of pH tests:", num_ph_tests.value())
print("The total number of probes used:", objective.value())
print("## end solving")