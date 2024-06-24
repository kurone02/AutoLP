from pulp import *

# Define the decision variables
# number of old vans
num_old_vans = LpVariable("NumOldVans", lowBound=0, cat='Integer')
# number of new vans
num_new_vans = LpVariable("NumNewVans", lowBound=0, upBound=30, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("SodaCompanyProblem", LpMinimize)

# Define the objective function
# minimize the total amount of pollution produced
objective = 50 * num_old_vans + 30 * num_new_vans
problem += objective

# Define the constraints
# total amount of soda bottles
problem += num_old_vans * 100 + num_new_vans * 80 >= 5000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of old vans:", num_old_vans.value())
print("The number of new vans:", num_new_vans.value())
print("The total amount of pollution produced:", objective.value())
print("## end solving")