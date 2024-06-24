from pulp import *

# Define the decision variables
hours_factory1 = LpVariable("HoursFactory1", lowBound=0, cat='Continuous')
hours_factory2 = LpVariable("HoursFactory2", lowBound=0, cat='Continuous')

# Define the question as a maximum or minimum problem
problem = LpProblem("TeddyBearCompany", LpMinimize)

# Define the objective function
objective = 300 * hours_factory1 + 600 * hours_factory2
# minimize the total cost of production
problem += objective

# Define the constraints
# the total number of black teddy bears produced must be at least 20
problem += 5 * hours_factory1 + 10 * hours_factory2 >= 20
# the total number of white teddy bears produced must be at least 5
problem += 6 * hours_factory1 + 10 * hours_factory2 >= 5
# the total number of brown teddy bears produced must be at least 15
problem += 3 * hours_factory1 >= 15

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("Hours to run factory 1:", hours_factory1.value())
print("Hours to run factory 2:", hours_factory2.value())
print("The total cost of production:", objective.value())
print("## end solving")