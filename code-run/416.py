from pulp import *

# Define the decision variables
num_day_phone = LpVariable("NumDayPhone", lowBound=0, cat='Integer')
num_night_phone = LpVariable("NumNightPhone", lowBound=0, cat='Integer')
num_day_personal = LpVariable("NumDayPersonal", lowBound=0, cat='Integer')
num_night_personal = LpVariable("NumNightPersonal", lowBound=0, cat='Integer')

# Define the question as a minimum or maximum problem
problem = LpProblem("CharitiesProblem", LpMaximize)

# Define the objective function
# maximize the total donations
objective = 2 * num_day_phone + 4 * num_day_personal + 3 * num_night_phone + 7 * num_night_personal
problem += objective

# Define the constraints
# maximum personal contacts
problem += num_day_personal + num_night_personal <= 300
# volunteer hours for day
problem += 6 * num_day_phone + 15 * num_day_personal <= 20 * 60
# volunteer hours for night
problem += 5 * num_night_phone + 12 * num_night_personal <= 40 * 60

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("Number of day phone interviews:", num_day_phone.value())
print("Number of night phone interviews:", num_night_phone.value())
print("Number of day personal interviews:", num_day_personal.value())
print("Number of night personal interviews:", num_night_personal.value())
print("Total donations:", objective.value())
print("## end solving")