from pulp import *

# Define the decision variables
x1 = LpVariable("x1", lowBound=0, cat='Continuous')
x2 = LpVariable("x2", lowBound=0, cat='Continuous')

# Define the problem
problem = LpProblem("SimpleLinearProgram", LpMaximize)

# Define the objective function
problem += x1 + x2, "Z"

# Define the constraints
problem += x2 - x1 <= 1
problem += x1 + 6*x2 <= 15
problem += 4*x1 - x2 <= 10

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The value of x1:", x1.value())
print("The value of x2:", x2.value())
print("The maximum value of x1 + x2:", value(problem.objective))
print("## end solving")