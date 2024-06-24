from pulp import *

# Define the decision variables
num_containers = LpVariable("NumContainers", lowBound=15, cat='Integer')
num_trucks = LpVariable("NumTrucks", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("OilAndGasCompany", LpMinimize)

# Define the objective function
problem += num_containers + num_trucks

# Define the constraints
problem  += 2*num_trucks <= num_containers # problem += num_trucks <= num_containers / 2
problem += 30 * num_containers + 40 * num_trucks >= 2000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of containers:", num_containers.value())
print("The number of trucks:", num_trucks.value())
print("The total number of containers and trucks:", value(problem.objective))
print("## end solving")