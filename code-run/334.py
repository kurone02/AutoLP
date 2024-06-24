from pulp import *

# Define the decision variables
# number of cups of spinach
num_cups_spinach = LpVariable("CupsSpinach", lowBound=0, cat='Integer')
# number of cups of soybeans
num_cups_soybeans = LpVariable("CupsSoybeans", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("NursesProblem", LpMaximize)

# Define the objective function
# maximize the total caloric intake
objective = 30 * num_cups_spinach + 100 * num_cups_soybeans
problem += objective

# Define the constraints
# total fibre intake
problem += 100 * num_cups_spinach + 80 * num_cups_soybeans >= 12000
# total iron intake
problem += 5 * num_cups_spinach + 12 * num_cups_soybeans >= 300
# number of cups of spinach must exceed the number of cups of soybeans
problem += num_cups_spinach >= 1 + num_cups_soybeans

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of cups of spinach:", num_cups_spinach.value())
print("The number of cups of soybeans:", num_cups_soybeans.value())
print("The total caloric intake:", objective.value())
print("## end solving")