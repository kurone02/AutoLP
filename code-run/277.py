from pulp import *

# Define the decision variables
# number of math workbooks
num_math_workbooks = LpVariable("NumMathWorkbooks", lowBound=40, upBound=140, cat='Integer')
# number of English workbooks
num_english_workbooks = LpVariable("NumEnglishWorkbooks", lowBound=60, upBound=170, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("WorkbookProfitMaximization", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 15 * num_math_workbooks + 17 * num_english_workbooks
problem += objective

# Define the constraints
# minimum demand for math workbooks
problem += num_math_workbooks >= 40
# minimum demand for English workbooks
problem += num_english_workbooks >= 60
# maximum demand for math workbooks
problem += num_math_workbooks <= 140
# maximum demand for English workbooks
problem += num_english_workbooks <= 170
# minimum total workbooks
problem += num_math_workbooks + num_english_workbooks >= 200

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of math workbooks:", num_math_workbooks.value())
print("The number of English workbooks:", num_english_workbooks.value())
print("The total profit:", objective.value())
print("## end solving")