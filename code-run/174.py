from pulp import *

# Define the decision variables
X = [LpVariable("X" + str(i), lowBound=0, cat='Integer') for i in range(7)]

# Define the problem
problem = LpProblem("MinWorkforceProblem", LpMinimize)

# Define the objective function
objective = sum(X[i] for i in range(7))
problem += objective

# Define the constraints
problem += X[0] + X[1] + X[2] + X[3] + X[4] >= 15
problem += X[1] + X[2] + X[3] + X[4] + X[5] >= 13
problem += X[2] + X[3] + X[4] + X[5] + X[6] >= 15
problem += X[3] + X[4] + X[5] + X[6] + X[0] >= 18
problem += X[4] + X[5] + X[6] + X[0] + X[1] >= 14
problem += X[5] + X[6] + X[0] + X[1] + X[2] >= 16
problem += X[6] + X[0] + X[1] + X[2] + X[3] >= 10

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The minimum number of workers needed:", value(objective))
print("Number of workers starting on Monday:", value(X[0]))
print("Number of workers starting on Tuesday:", value(X[1]))
print("Number of workers starting on Wednesday:", value(X[2]))
print("Number of workers starting on Thursday:", value(X[3]))
print("Number of workers starting on Friday:", value(X[4]))
print("Number of workers starting on Saturday:", value(X[5]))
print("Number of workers starting on Sunday:", value(X[6]))
print("## end solving")