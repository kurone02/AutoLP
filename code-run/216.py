from pulp import *

# Define the decision variables
# number of almonds
num_almonds = LpVariable("NumAlmonds", lowBound=0, cat='Integer')
# number of cashews
num_cashews = LpVariable("NumCashews", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("WomanNutritionProblem", LpMinimize)

# Define the objective function
# minimize the total fat intake
objective = 15 * num_almonds + 12 * num_cashews
problem += objective

# Define the constraints
# total calories
problem += 200 * num_almonds + 300 * num_cashews >= 10000
# total protein
problem += 20 * num_almonds + 25 * num_cashews >= 800
# at least twice as many servings of almonds as cashews
problem += num_almonds >= 2 * num_cashews

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of servings of almonds:", num_almonds.value())
print("The number of servings of cashews:", num_cashews.value())
print("The total fat intake:", objective.value())
print("## end solving")