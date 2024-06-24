from pulp import *

# Define the variables
num_pill_vaccines = LpVariable("NumPillVaccines", lowBound=30, cat='Integer')
num_shot_vaccines = LpVariable("NumShotVaccines", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("VaccineProblem", LpMaximize)
objective = num_pill_vaccines + num_shot_vaccines
problem += objective

# Define the constraints
problem += 10 * num_pill_vaccines + 20 * num_shot_vaccines <= 10000
problem += num_shot_vaccines >= 3 * num_pill_vaccines
problem += num_pill_vaccines >= 30

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of pill vaccines:", value(num_pill_vaccines))
print("The number of shot vaccines:", value(num_shot_vaccines))
print("The total number of patients vaccinated:", value(objective))
print("## end solving")