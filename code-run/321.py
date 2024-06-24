from pulp import *

# Define the decision variables
# number of blood tests
num_blood_tests = LpVariable("NumBloodTests", lowBound=0, cat='Integer')
# number of ear tests
num_ear_tests = LpVariable("NumEarTests", lowBound=12, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("ClinicTestProblem", LpMaximize)

# Define the objective function
# maximize the total number of tests
objective = num_blood_tests + num_ear_tests
problem += objective

# Define the constraints
# total time of blood tests
problem += 30 * num_blood_tests <= 7525
# total time of ear tests
problem += 5 * num_ear_tests <= 7525
# three times as many blood tests as ear tests
problem += num_blood_tests >= 3 * num_ear_tests
# minimum ear tests
problem += num_ear_tests >= 12

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of blood tests:", num_blood_tests.value())
print("The number of ear tests:", num_ear_tests.value())
print("The total number of tests performed:", objective.value())
print("## end solving")