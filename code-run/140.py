from pulp import *

# Define the decision variables
# number of small branches
num_small_branches = LpVariable("SmallBranches", lowBound=0, cat='Integer')
# number of large branches
num_large_branches = LpVariable("LargeBranches", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("BankBranchProblem", LpMinimize)

# Define the objective function
# minimize the total number of branches
problem += num_small_branches + num_large_branches

# Define the constraints
# total bank tellers
problem += 10 * num_small_branches + 15 * num_large_branches <= 200
# total customers served
problem += 50 * num_small_branches + 100 * num_large_branches >= 1200

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of small branches:", num_small_branches.value())
print("The number of large branches:", num_large_branches.value())
print("The total number of branches:", (num_small_branches.value() + num_large_branches.value()))
print("## end solving")