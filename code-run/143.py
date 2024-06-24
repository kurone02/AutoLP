from pulp import *

# Define the decision variables
# number of acres to be used by the traditional machine
acres_traditional = LpVariable("AcresTraditional", lowBound=0, cat='Integer')
# number of acres to be used by the modern machine
acres_modern = LpVariable("AcresModern", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("TeaEstateProblem", LpMaximize)

# Define the objective function
# maximize the total amount of tea leaves that can be picked
objective = 30 * acres_traditional + 40 * acres_modern
problem += objective

# Define the constraints
# total acres available
problem += acres_traditional + acres_modern <= 500
# total fuel available
problem += 20 * acres_traditional + 15 * acres_modern <= 9000
# total waste produced
problem += 10 * acres_traditional + 15 * acres_modern <= 6000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The acres for traditional machine:", acres_traditional.value())
print("The acres for modern machine:", acres_modern.value())
print("The amount of tea leaves picked:", objective.value())
print("## end solving")