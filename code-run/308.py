from pulp import *

# Define the variables
num_cans = LpVariable("NumCans", lowBound=0, cat='Integer')
num_bottles = LpVariable("NumBottles", lowBound=100, cat='Integer')

# Define the problem
problem = LpProblem("SodaCompanyProblem", LpMinimize)
objective = num_cans + num_bottles
problem += objective

# Define the constraints
problem += 250 * num_cans + 1000 * num_bottles >= 1000000
problem += num_cans >= 3 * num_bottles
problem += num_bottles >= 100

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of soda cans:", value(num_cans))
print("The number of soda bottles:", value(num_bottles))
print("The total number of units produced:", value(objective))
print("## end solving")