from pulp import *

# Define the decision variables
# number of temperature checks
num_temp_checks = LpVariable("NumTempChecks", lowBound=0, cat='Integer')
# number of blood tests
num_blood_tests = LpVariable("NumBloodTests", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("DiseaseTestingProblem", LpMaximize)

# Define the objective function
# maximize the total number of patients seen
objective = num_temp_checks + num_blood_tests
problem += objective

# Define the constraints
# total staff minutes available
problem += 2 * num_temp_checks + 10 * num_blood_tests <= 22000
# minimum number of blood tests
problem += num_blood_tests >= 45
# temperature check constraint
problem += num_temp_checks >= 5 * num_blood_tests

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of temperature checks:", num_temp_checks.value())
print("The number of blood tests:", num_blood_tests.value())
print("The total number of patients seen:", objective.value())
print("## end solving")