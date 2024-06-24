from pulp import *

# Define the decision variables
# number of staff teachers
num_staff_teachers = LpVariable("NumStaffTeachers", lowBound=0, cat='Integer')
# number of substitute teachers
num_sub_teachers = LpVariable("NumSubTeachers", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("SchoolTeachingProblem", LpMinimize)

# Define the objective function
# minimize the total number of teachers
problem += num_staff_teachers + num_sub_teachers

# Define the constraints
# total teaching hours
problem += 6 * num_staff_teachers + 3 * num_sub_teachers >= 1000
# total cost
problem += 300 * num_staff_teachers + 100 * num_sub_teachers <= 40000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of staff teachers:", num_staff_teachers.value())
print("The number of substitute teachers:", num_sub_teachers.value())
print("The total number of teachers:", value(problem.objective))
print("## end solving")