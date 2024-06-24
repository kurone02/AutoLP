from pulp import *

# Define the decision variables
# number of small kegs
num_small_kegs = LpVariable("NumSmallKegs", lowBound=0, cat='Integer')
# number of large kegs
num_large_kegs = LpVariable("NumLargeKegs", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("WaterSalesmanProblem", LpMaximize)

# Define the objective function
# maximize the total amount of glacial water transported
objective = 40 * num_small_kegs + 100 * num_large_kegs
problem += objective

# Define the constraints
# small kegs availability
problem += num_small_kegs <= 30
# large kegs availability
problem += num_large_kegs <= 10
# at least twice as many small kegs must be used than large kegs
problem += num_small_kegs >= 2 * num_large_kegs
# total kegs constraint
problem += num_small_kegs + num_large_kegs <= 25
# at least 5 kegs must be large
problem += num_large_kegs >= 5

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of small kegs:", num_small_kegs.value())
print("The number of large kegs:", num_large_kegs.value())
print("The total liters of glacial water transported:", objective.value())
print("## end solving")