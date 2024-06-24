from pulp import *

# Define the decision variables
num_zodiac_pills = LpVariable("NumZodiacPills", lowBound=0, cat='Integer')
num_sunny_pills = LpVariable("NumSunnyPills", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("MedicineProblem", LpMinimize)

# Define the objective function
problem += 1 * num_zodiac_pills + 3 * num_sunny_pills

# Define the constraints
problem += 1.3 * num_zodiac_pills + 1.2 * num_sunny_pills >= 5
problem += 1.5 * num_zodiac_pills + 5 * num_sunny_pills >= 10

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of Zodiac pills:", num_zodiac_pills.value())
print("The number of Sunny pills:", num_sunny_pills.value())
print("The total cost:", problem.objective.value())
print("## end solving")