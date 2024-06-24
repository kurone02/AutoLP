from pulp import *

# Define the variables
num_cows = LpVariable("NumCows", lowBound=0, cat='Integer')
num_elephants = LpVariable("NumElephants", lowBound=0, cat='Integer')

# Define the question as a minimum problem
problem = LpProblem("AnimalTransportationProblem", LpMinimize)

# Define the objective function
problem += num_cows + num_elephants

# Define the constraints
problem += 20 * num_cows + 50 * num_elephants >= 1000
problem += num_elephants <= num_cows
problem += num_elephants <= 2 * num_cows

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of cows:", num_cows.value())
print("The number of elephants:", num_elephants.value())
print("The total number of animals used:", value(problem.objective))
print("## end solving")