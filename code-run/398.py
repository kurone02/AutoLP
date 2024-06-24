from pulp import *

# Define the data
time_matrix = [
    [0, 10, 20, 30, 30, 20],
    [10, 0, 25, 35, 20, 10],
    [20, 25, 0, 15, 30, 20],
    [30, 35, 15, 0, 15, 25],
    [30, 20, 30, 15, 0, 14],
    [20, 10, 20, 25, 14, 0]
]

cities = range(6)
M = 1000

# Create the problem
prob = LpProblem("FireStationLocation", LpMinimize)

# Create the variables
x = LpVariable.dicts("FireStation", cities, 0, 1, LpInteger)
y = LpVariable.dicts("Coverage", (cities, cities), 0, 1, LpInteger)

# Add the objective function
prob += lpSum([x[i] for i in cities])

# Add the constraints
for j in cities:
    prob += lpSum([y[i][j] for i in cities]) >= 1

for i in cities:
    prob += lpSum([y[i][j] for j in cities]) - M*(1-x[i]) >= 0

# Solve the problem
status = prob.solve(PULP_CBC_CMD(msg=0))

# Print the solution
print("## start solving")
print("The optimal number of fire stations to be built is:", int(value(prob.objective)))
for i in cities:
    print(f"Whether a fire station should be built in City {i+1}:", int(value(x[i])))
print("## end solving")