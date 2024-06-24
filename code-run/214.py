from pulp import *

# Define the decision variables
# number of vans used
num_vans = LpVariable("NumVans", lowBound=0, cat='Integer')
# number of trucks used
num_trucks = LpVariable("NumTrucks", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("ShoeCompanyProblem", LpMinimize)

# Define the objective function
# minimize the number of vans used
problem += num_vans

# Define the constraints
# number of trucks used cannot exceed the number of vans used
problem += num_trucks <= num_vans
# supply a minimum of 2000 pairs of shoes around the city
problem += num_vans * 50 + num_trucks * 100 >= 2000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of vans used:", num_vans.value())
print("The number of trucks used:", num_trucks.value())
print("## end solving")