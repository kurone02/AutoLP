from pulp import *

# Define the decision variables
# number of large pills
num_large_pills = LpVariable("NumLargePills", lowBound=100, cat='Integer')
# number of small pills
num_small_pills = LpVariable("NumSmallPills", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("MedicineLabProblem", LpMinimize)

# Define the objective function
# minimize the total amount of filler material used
objective = 2 * num_large_pills + 1 * num_small_pills
problem += objective

# Define the constraints
# total medicinal ingredients constraint
problem += 3 * num_large_pills + 2 * num_small_pills <= 1000
# large pills constraint
problem += num_large_pills >= 100
# small pills popularity constraint
problem += num_small_pills >= 0.6 * (num_large_pills + num_small_pills)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of large pills:", num_large_pills.value())
print("The number of small pills:", num_small_pills.value())
print("Total amount of filler material used:", objective.value())
print("## end solving")