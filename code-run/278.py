from pulp import *

# Define the decision variables
# number of full-weighted keyboards
num_full_weighted = LpVariable("NumFullWeighted", lowBound=0, cat='Integer')
# number of semi-weighted keyboards
num_semi_weighted = LpVariable("NumSemiWeighted", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("MusicCompanyProblem", LpMaximize)

# Define the objective function
# maximize the total revenue
objective = 2800 * num_full_weighted + 2400 * num_semi_weighted
problem += objective

# Define the constraints
# total oscillator chips
problem += 20 * num_full_weighted + 15 * num_semi_weighted <= 3500
# total working hours
problem  += num_full_weighted + num_semi_weighted <= 5.0 # problem += num_full_weighted + num_semi_weighted <= 6 / 1.2

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of full-weighted keyboards:", num_full_weighted.value())
print("The number of semi-weighted keyboards:", num_semi_weighted.value())
print("Total revenue:", objective.value())
print("## end solving")