from pulp import *

# Define the decision variables
# number of hours using method A
num_hours_method_A = LpVariable("HoursMethodA", lowBound=0, cat='Integer')
# number of hours using method B
num_hours_method_B = LpVariable("HoursMethodB", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("ResearchGroupProblem", LpMinimize)

# Define the objective function
# minimize the total time needed
objective = num_hours_method_A + num_hours_method_B
problem += objective

# Define the constraints
# total fabric produced
problem += 25 * num_hours_method_A + 45 * num_hours_method_B >= 1400
# total plastic produced
problem += 14 * num_hours_method_A + 25 * num_hours_method_B >= 1000
# total special element used
problem += 60 * num_hours_method_A + 65 * num_hours_method_B <= 3500

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of hours using method A:", num_hours_method_A.value())
print("The number of hours using method B:", num_hours_method_B.value())
print("The total time needed:", objective.value())
print("## end solving")