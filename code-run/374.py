from pulp import *

# Define the decision variables
x1 = LpVariable("Fertilizer1", lowBound=0, cat='Continuous')
x2 = LpVariable("Fertilizer2", lowBound=0, cat='Continuous')
x3 = LpVariable("Fertilizer3", lowBound=0, cat='Continuous')
x4 = LpVariable("Fertilizer4", lowBound=0, cat='Continuous')
x5 = LpVariable("Fertilizer5", lowBound=0, cat='Continuous')

# Define the problem
problem = LpProblem("FertilizerMixProblem", LpMinimize)

# Define the objective function
problem += 21.75 * x1 + 23.75 * x2 + 22.00 * x3 + 19.50 * x4 + 18.50 * x5

# Define the constraints
problem += 10 * x1 + 8 * x2 + 12 * x3 + 10 * x4 + 15 * x5 >= 10
problem += 10 * x1 + 8 * x2 + 12 * x3 + 10 * x4 + 15 * x5 <= 10.5
problem += 8 * x1 + 11 * x2 + 7 * x3 + 10 * x4 + 10 * x5 >= 8
problem += 8 * x1 + 11 * x2 + 7 * x3 + 10 * x4 + 10 * x5 <= 8.5
problem += 12 * x1 + 12 * x2 + 12 * x3 + 10 * x4 + 6 * x5 >= 12
problem += 12 * x1 + 12 * x2 + 12 * x3 + 10 * x4 + 6 * x5 <= 12.5

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The quantity of Fertilizer 1:", x1.value())
print("The quantity of Fertilizer 2:", x2.value())
print("The quantity of Fertilizer 3:", x3.value())
print("The quantity of Fertilizer 4:", x4.value())
print("The quantity of Fertilizer 5:", x5.value())
print("## end solving")