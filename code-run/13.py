from pulp import *

# Define the variables
num_crab_soup = LpVariable("NumCrabSoup", lowBound=0, cat='Integer')
num_lobster_soup = LpVariable("NumLobsterSoup", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("SoupStoreProblem", LpMaximize)
objective = 3 * num_crab_soup + 5 * num_lobster_soup
problem += objective

# Define the constraints
problem += 7 * num_crab_soup + 10 * num_lobster_soup <= 80
problem += 8 * num_crab_soup <= 65
problem += 5 * num_lobster_soup <= 55

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of servings of crab soup:", value(num_crab_soup))
print("The number of servings of lobster soup:", value(num_lobster_soup))
print("The total profit:", value(objective))
print("## end solving")