from pulp import *

# Define the decision variables
# number of regular wine to make per day
x1 = LpVariable("x1", lowBound=0, cat='Integer')
# number of premium wine to make per day
x2 = LpVariable("x2", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("WineProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 20 * x1 + 50 * x2
problem += objective

# Define the constraints
# current demand for the regular wine
problem += x1 <= 80
# current demand for the premium wine
problem += x2 <= 50
# total number of bottles
problem += x1 + x2 <= 120

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("Number of bottles of regular wine to make per day:", x1.value())
print("Number of bottles of premium wine to make per day:", x2.value())
print("Maximum profit per day:", objective.value())
print("## end solving")