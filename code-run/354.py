from pulp import *

# Define the decision variables
# number of coconut oil units
num_coconut = LpVariable("NumCoconut", lowBound=300, cat='Integer')
# number of lavender units
num_lavender = LpVariable("NumLavender", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("BodyWashProblem", LpMinimize)

# Define the objective function
# minimize the total effective time
objective = 0.7 * num_coconut + 0.9 * num_lavender
problem += objective

# Define the constraints
# at least 300 units of coconut oil
problem += num_coconut >= 300
# at most 550 units of both ingredients
problem += num_coconut + num_lavender <= 550
# at most thrice the amount of coconut oil as lavenders
problem += num_lavender <= 3 * num_coconut

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of coconut oil units:", num_coconut.value())
print("The number of lavender units:", num_lavender.value())
print("The minimum effective time:", objective.value())
print("## end solving")