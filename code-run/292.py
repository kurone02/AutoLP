from pulp import *

# Define the decision variables
# number of ultrasound technicians
num_ultrasound = LpVariable("NumUltrasound", lowBound=0, cat='Integer')
# number of graduate researchers
num_researchers = LpVariable("NumResearchers", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("HospitalSchedulingProblem", LpMinimize)

# Define the objective function
# minimize the total number of workers
objective = num_ultrasound + num_researchers
problem += objective

# Define the constraints
# total hours of ultrasound services
problem += 8 * num_ultrasound + 5 * num_researchers >= 100
problem += 8 * num_ultrasound + 5 * num_researchers <= 100
# total cost of ultrasound technicians
problem += 300 * num_ultrasound <= 14000
# total cost of researchers
problem += 100 * num_researchers <= 14000
# ultrasound technician shifts
problem += num_ultrasound >= 2 * num_researchers

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of ultrasound technicians:", num_ultrasound.value())
print("The number of graduate researchers:", num_researchers.value())
print("## end solving")