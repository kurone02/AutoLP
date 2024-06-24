from pulp import *

# Define the decision variables
x1 = LpVariable("x1", cat='Binary')
x2 = LpVariable("x2", cat='Binary')
x3 = LpVariable("x3", cat='Binary')
x4 = LpVariable("x4", cat='Binary')

# Define the problem
problem = LpProblem("KnapsackProblem", LpMaximize)

# Define the objective function
problem += 15*x1 + 25*x2 + 12*x3 + 10*x4

# Define the constraints
problem += 3*x1 + 6*x2 + 5*x3 + 5*x4 <= 12

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The decision to put item 1 in the knapsack:", x1.varValue)
print("The decision to put item 2 in the knapsack:", x2.varValue)
print("The decision to put item 3 in the knapsack:", x3.varValue)
print("The decision to put item 4 in the knapsack:", x4.varValue)
print("The maximum total value of the knapsack:", value(problem.objective))
print("## end solving")