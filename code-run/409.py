from pulp import *

# Define the problem
prob = LpProblem("SchoolBusingProblem", LpMinimize)

# Define the decision variables
districts = ['North', 'East', 'South', 'West', 'Central']
schools = ['Central', 'West', 'South']
x = LpVariable.dicts("students", (districts, schools), 0, None, LpInteger)

# Define the objective function
prob += lpSum([x[i][j] * distance[i][j] for i in districts for j in schools])

# Define the constraints
student_population = {'North': 700, 'East': 900, 'South': 500, 'West': 600, 'Central': 800}
school_capacity = {'Central': 1200, 'West': 1200, 'South': 1200}
for i in districts:
    prob += lpSum([x[i][j] for j in schools]) <= student_population[i]
for j in schools:
    prob += lpSum([x[i][j] for i in districts]) <= school_capacity[j]

# Solve the problem
status = prob.solve(PULP_CBC_CMD(msg=0))

# Print the results
print("## start solving")
for i in districts:
    for j in schools:
        print(f"The number of students from {i} to {j}: {value(x[i][j])}")
print(f"Total busing miles traveled: {value(prob.objective)}")
print("## end solving")