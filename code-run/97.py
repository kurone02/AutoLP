from pulp import *

# Define the decision variables
# number of loaves of bread to produce
num_bread = LpVariable("NumBread", lowBound=0, cat='Integer')
# number of batches of cookies to produce
num_cookies = LpVariable("NumCookies", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("BakeryProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 5 * num_bread + 3 * num_cookies
problem += objective

# Define the constraints
# total time for the stand-mixer
problem += 1 * num_bread + 0.5 * num_cookies <= 3000
# total time for the oven
problem += 3 * num_bread + 1 * num_cookies <= 3000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of loaves of bread:", num_bread.value())
print("The number of batches of cookies:", num_cookies.value())
print("Total profit:", objective.value())
print("## end solving")