from pulp import *

# Define the decision variables
# number of supplement A pills
num_supp_A = LpVariable("SuppAPills", lowBound=0, cat='Integer')
# number of supplement B pills
num_supp_B = LpVariable("SuppBPills", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("DietProblem", LpMinimize)

# Define the objective function
# minimize the total cost
objective = 2 * num_supp_A + 3 * num_supp_B
problem += objective

# Define the constraints
# iron requirement
problem += 5 * num_supp_A + 4 * num_supp_B >= 40
# calcium requirement
problem += 10 * num_supp_A + 15 * num_supp_B >= 50

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of supplement A pills:", num_supp_A.value())
print("The number of supplement B pills:", num_supp_B.value())
print("The total cost:", objective.value())
print("## end solving")