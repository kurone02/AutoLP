from pulp import *

# Define the decision variables
# number of perfume bottles to fill
num_perfume_bottles = LpVariable("NumPerfumeBottles", lowBound=60, cat='Integer')
# number of cologne bottles to fill
num_cologne_bottles = LpVariable("NumCologneBottles", lowBound=40, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("MakeupCompanyProfitProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 50 * num_perfume_bottles + 60 * num_cologne_bottles
problem += objective

# Define the constraints
# total time available
problem += 2 * num_perfume_bottles + 2.5 * num_cologne_bottles <= 700
# at least 60 perfume bottles
problem += num_perfume_bottles >= 60
# at least 40 cologne bottles
problem += num_cologne_bottles >= 40

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of perfume bottles filled:", num_perfume_bottles.value())
print("The number of cologne bottles filled:", num_cologne_bottles.value())
print("Total profit:", objective.value())
print("## end solving")