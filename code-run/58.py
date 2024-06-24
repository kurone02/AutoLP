from pulp import *

# Define the decision variables
num_cherry = LpVariable("NumCherry", lowBound=0, cat='Integer')
num_peach = LpVariable("NumPeach", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("CandyProblem", LpMinimize)

# Define the objective function
objective = 0.10 * num_cherry + 0.12 * num_peach
problem += objective

# Define the constraints
problem += 2 * num_cherry + 1 * num_peach >= 50
problem += 3 * num_cherry + 4 * num_peach >= 60
problem += num_cherry <= 10

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of sour cherry candies:", num_cherry.value())
print("The number of sour peach candies:", num_peach.value())
print("The total cost of the candies:", objective.value())
print("## end solving")