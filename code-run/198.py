from pulp import *

# Define the decision variables
x_1 = LpVariable("PhoneDay", lowBound=0, cat='Integer')
x_2 = LpVariable("PhoneNight", lowBound=0, cat='Integer')
x_3 = LpVariable("PersonalDay", lowBound=0, cat='Integer')
x_4 = LpVariable("PersonalNight", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("CharitiesProblem", LpMaximize)

# Define the objective function
problem += 2 * x_1 + 3 * x_2 + 4 * x_3 + 7 * x_4

# Define the constraints
problem += 6 * x_1 + 5 * x_2 <= 20
problem += 6 * x_1 + 5 * x_2 <= 40
problem += 15 * x_3 + 12 * x_4 <= 20
problem += 15 * x_3 + 12 * x_4 <= 40
problem += x_3 + x_4 <= 300

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("Number of day phone interviews:", value(x_1))
print("Number of night phone interviews:", value(x_2))
print("Number of day personal interviews:", value(x_3))
print("Number of night personal interviews:", value(x_4))
print("Total donations:", value(problem.objective))
print("## end solving")