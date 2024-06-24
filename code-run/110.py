from pulp import *

# Define the variables
num_pill_A = LpVariable("NumPillA", lowBound=0, cat='Integer')
num_pill_B = LpVariable("NumPillB", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("MedicineProblem", LpMinimize)
objective = 4 * num_pill_A + 5 * num_pill_B
problem += objective

# Define the constraints
problem += 3 * num_pill_A + 6 * num_pill_B >= 40
problem += 5 * num_pill_A + 1 * num_pill_B >= 50

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of pill A:", value(num_pill_A))
print("The number of pill B:", value(num_pill_B))
print("The total cost for the patient:", value(objective))
print("## end solving")