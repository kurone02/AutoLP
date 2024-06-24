from pulp import *

# Define the decision variables
x1 = LpVariable("RegularCars", lowBound=0, cat='Integer')
x2 = LpVariable("PremiumCars", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("CarManufacturingProblem", LpMaximize)

# Define the objective function
problem += 5000 * x1 + 8500 * x2

# Define the constraints
problem += x1 <= 8
problem += x2 <= 6
problem += x1 + x2 <= 12

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of regular models:", x1.value())
print("The number of premium models:", x2.value())
print("The total profit:", value(problem.objective))
print("## end solving")