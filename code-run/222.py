from pulp import *

# Define the decision variables
# number of small containers
num_small_containers = LpVariable("NumSmallContainers", lowBound=3, cat='Integer')
# number of large containers
num_large_containers = LpVariable("NumLargeContainers", lowBound=5, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("SandCompanyProblem", LpMaximize)

# Define the objective function
# maximize the total sand delivered
objective = 20 * num_small_containers + 50 * num_large_containers
problem += objective

# Define the constraints
# total people used
problem += num_small_containers + 3 * num_large_containers <= 100
# number of small containers
problem += num_small_containers == 3 * num_large_containers
# minimum number of small and large containers
problem += num_small_containers >= 5
problem += num_large_containers >= 3

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of small containers:", num_small_containers.value())
print("The number of large containers:", num_large_containers.value())
print("The amount of sand delivered:", objective.value())
print("## end solving")