from pulp import *

# Define the problem
prob = LpProblem("FireStationLocation", LpMinimize)

# Define the decision variables
# x[i] = 1 if a fire station is built in city i, 0 otherwise
x = [LpVariable("x"+str(i), cat='Binary') for i in range(6)]

# Define the objective function
prob += lpSum(x)

# Define the constraints
# Ensure that each city is within a 15 minute drive from at least one fire station
for i in range(6):
    prob += lpSum([x[j] for j in range(6) if j != i and travel_time[i][j] <= 15]) >= 1

# Solve the problem
prob.solve()

# Output the answer
print("## start solving")
print("The optimal number of fire stations to be built is:", int(value(prob.objective)))
for i in range(6):
    print("Whether a fire stations should be built in City "+str(i+1)+":", int(value(x[i])))
print("## end solving")