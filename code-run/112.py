from pulp import *

# Define the decision variables
# number of chocolate ice cream gallons
num_chocolate = LpVariable("NumChocolate", lowBound=5, upBound=10, cat='Continuous')
# number of vanilla ice cream gallons
num_vanilla = LpVariable("NumVanilla", lowBound=5, upBound=8, cat='Continuous') 

# Define the question as a minimum or maximum problem
problem = LpProblem("IceCreamProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 200 * num_chocolate + 300 * num_vanilla
problem += objective

# Define the constraints
# total time constraint
problem += num_chocolate + 2 * num_vanilla <= 30
# total workers constraint
problem += num_chocolate + 2 * num_vanilla >= 6

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("Gallons of chocolate ice cream:", num_chocolate.value())
print("Gallons of vanilla ice cream:", num_vanilla.value())
print("Total profit:", objective.value())
print("## end solving")