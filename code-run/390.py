from pulp import *

# Define the problem
prob = LpProblem("MinimumWorkers", LpMinimize)

# Define the variables
days = list(range(11))
x = LpVariable.dicts("workers", days, 0, cat='Integer')

# Define the objective function
prob += lpSum([x[i] for i in days])

# Define the constraints
prob += lpSum([x[i] for i in range(5)]) >= 15
prob += lpSum([x[i] for i in range(1, 6)]) >= 13
prob += lpSum([x[i] for i in range(2, 7)]) >= 15
prob += lpSum([x[i] for i in range(3, 8)]) >= 18
prob += lpSum([x[i] for i in range(4, 9)]) >= 14
prob += lpSum([x[i] for i in range(5, 10)]) >= 16
prob += lpSum([x[i] for i in range(6, 11)]) >= 10

# Solve the problem
prob.solve()

# Print the status of the solution
print("## start solving")
print("Status:", LpStatus[prob.status])
print("The minimum number of workers needed is:", value(prob.objective))
print("Number of workers starting on Monday:", x[0].value())
print("Number of workers starting on Tuesday:", x[1].value())
print("Number of workers starting on Wednesday:", x[2].value())
print("Number of workers starting on Thursday:", x[3].value())
print("Number of workers starting on Friday:", x[4].value())
print("Number of workers starting on Saturday:", x[5].value())
print("Number of workers starting on Sunday:", x[6].value())
print("## end solving")