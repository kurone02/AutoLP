from pulp import *

# Define the distance matrix
time = [[0, 10, 20, 30, 30, 20],
        [10, 0, 25, 35, 20, 10],
        [20, 25, 0, 15, 30, 20],
        [30, 35, 15, 0, 15, 25],
        [30, 20, 30, 15, 0, 14],
        [20, 10, 20, 25, 14, 0]]

# Define the problem
problem = LpProblem("FireStationLocation", LpMinimize)

# Define the variables
x = [LpVariable("x" + str(i), cat='Binary') for i in range(6)]

# Define the objective function
problem += lpSum(x)

# Define the constraints
for j in range(6):
    problem += lpSum([x[i] for i in range(6) if time[i][j] <= 15]) >= 1

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The optimal number of fire stations to be built is:", int(value(problem.objective)))
for i in range(6):
    print("Whether a fire station should be built in City " + str(i + 1) + ": " + str(int(value(x[i]))))
print("## end solving")