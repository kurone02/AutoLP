from pulp import *

# Define the decision variables
# number of earl grey teabags
num_earl_grey = LpVariable("NumEarlGrey", lowBound=0, cat='Integer')
# number of English breakfast teabags
num_english_breakfast = LpVariable("NumEnglishBreakfast", lowBound=20, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("TeaProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 0.30 * num_earl_grey + 0.25 * num_english_breakfast
problem += objective

# Define the constraints
# total black tea available
problem += 25 * num_earl_grey + 20 * num_english_breakfast <= 3000
# demand for earl grey teabags
problem += num_earl_grey >= 4 * num_english_breakfast
# minimum English breakfast teabags
problem += num_english_breakfast >= 20

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of earl grey teabags:", num_earl_grey.value())
print("The number of English breakfast teabags:", num_english_breakfast.value())
print("The total profit:", objective.value())
print("## end solving")