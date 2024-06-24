from pulp import *

# Define the decision variables
num_vans = LpVariable("NumVans", lowBound=0, cat='Integer')
num_minibuses = LpVariable("NumMinibuses", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("SchoolTransportationProblem", LpMinimize)

# Define the objective function
# minimize the total pollution produced
objective = 7 * num_vans + 10 * num_minibuses
problem += objective

# Define the constraints
# minimum kids constraint
problem += 6 * num_vans + 10 * num_minibuses >= 150
# max minibuses constraint
problem += num_minibuses <= 10
# more vans than minibuses constraint
problem += num_vans >= 1 + num_minibuses

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of vans used:", num_vans.value())
print("The number of minibuses used:", num_minibuses.value())
print("The total pollution produced:", objective.value())
print("## end solving")