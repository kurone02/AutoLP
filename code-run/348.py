from pulp import *

# Define the decision variables
hours_special = LpVariable("HoursSpecial", lowBound=0, cat='Continuous')
hours_common = LpVariable("HoursCommon", lowBound=0, cat='Continuous') 

# Define the question as a minimum or maximum problem
problem = LpProblem("AnnotationProblem", LpMinimize)

# Define the objective function
# minimize the total cost
objective = 100 * hours_special + 72 * hours_common
problem += objective

# Define the constraints
# total number of images to annotate
problem += hours_special * 60 + hours_common * 40 >= 10000
# at least a third of work must be allocated to the specialized company
problem  += 3*hours_special >= 2*hours_common + 2*hours_special # problem += hours_special >= 2/3 * (hours_special + hours_common)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The hours for the specialized company:", hours_special.value())
print("The hours for the common company:", hours_common.value())
print("The total cost:", objective.value())
print("## end solving")