from pulp import *

# Define the decision variables
# number of first-dose vaccines
num_first_dose = LpVariable("NumFirstDose", lowBound=0, cat='Integer')
# number of second-dose vaccines
num_second_dose = LpVariable("NumSecondDose", lowBound=40, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("BiotechProblem", LpMinimize)

# Define the objective function
# minimize the total amount of gelatine used
objective = 20 * num_first_dose + 60 * num_second_dose
problem += objective

# Define the constraints
# antibiotics constraint
problem += 30 * num_first_dose + 65 * num_second_dose <= 35000
# dose order constraint
problem += num_first_dose >= 1 + num_second_dose
# second-dose vaccine constraint
problem += num_second_dose >= 40

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of first-dose vaccines:", num_first_dose.value())
print("The number of second-dose vaccines:", num_second_dose.value())
print("The amount of gelatine used:", objective.value())
print("## end solving")