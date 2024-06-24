from pulp import *

# Define the decision variables
# number of carts
num_carts = LpVariable("NumCarts", lowBound=0, cat='Integer')
# number of trolleys
num_trolleys = LpVariable("NumTrolleys", lowBound=12, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("ConcertOrganizerProblem", LpMinimize)

# Define the objective function
# minimize the total number of workers
objective = 2 * num_carts + 4 * num_trolleys
problem += objective

# Define the constraints
# total rate of equipment
problem += 5 * num_carts + 7 * num_trolleys >= 100
# maximum percentage of trolleys
problem += num_trolleys <= 0.4 * (num_carts + num_trolleys)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of carts:", num_carts.value())
print("The number of trolleys:", num_trolleys.value())
print("The minimum number of workers required:", objective.value())
print("## end solving")