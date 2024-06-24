from pulp import *

# Define the decision variables
# number of student painters
num_student_painters = LpVariable("NumStudentPainters", lowBound=0, cat='Integer')
# number of full-time painters
num_full_time_painters = LpVariable("NumFullTimePainters", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("PaintingCompanyProblem", LpMinimize)

# Define the objective function
# minimize the total wage bill
objective = 200 * num_student_painters + 500 * num_full_time_painters
problem += objective

# Define the constraints
# total number of painters
problem += num_student_painters + num_full_time_painters >= 100
# number of full-time painters
problem += num_full_time_painters >= 30
# number of full-time painters should be at least half the number of student painters
problem += num_full_time_painters - num_student_painters >= 0

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of student painters:", num_student_painters.value())
print("The number of full-time painters:", num_full_time_painters.value())
print("The total wage bill:", objective.value())
print("## end solving")