from pulp import *

# Define the decision variables
# number of adhesives packages produced daily
num_adhesives = LpVariable("NumAdhesives", lowBound=0, cat='Integer')
# number of plasticizers packages produced daily
num_plasticizers = LpVariable("NumPlasticizers", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("CEChemicalsProblem", LpMaximize)

# Define the objective function
# maximize the total revenue
objective = 8.5 * num_adhesives + 11.5 * num_plasticizers
problem += objective

# Define the constraints
# total time on automatic devices
problem += 6 * num_adhesives + 8 * num_plasticizers <= 450
# total time on human-operated devices
problem += 5 * num_adhesives + 4 * num_plasticizers <= 450

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of packages of adhesives produced daily:", num_adhesives.value())
print("The number of packages of plasticizers produced daily:", num_plasticizers.value())
print("The maximum daily revenue:", objective.value())
print("## end solving")