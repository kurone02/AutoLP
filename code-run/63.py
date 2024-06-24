from pulp import *

# Define the decision variables
# number of Special Formula capsules
num_special_formula = LpVariable("NumSpecialFormula", lowBound=0, cat='Integer')
# number of One Daily capsules
num_one_daily = LpVariable("NumOneDaily", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("VitaminPurchaseProblem", LpMinimize)

# Define the objective function
# minimize the total cost
objective = 0.5 * num_special_formula + 0.2 * num_one_daily
problem += objective

# Define the constraints
# vitamin A requirement
problem += 4 * num_special_formula + 3 * num_one_daily >= 25
# vitamin B requirement
problem += 5 * num_special_formula + 7 * num_one_daily >= 40

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of Special Formula capsules:", num_special_formula.value())
print("The number of One Daily capsules:", num_one_daily.value())
print("The total cost:", objective.value())
print("## end solving")