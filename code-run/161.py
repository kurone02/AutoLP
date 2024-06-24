from pulp import *

# Define the decision variables
num_ij_10k = LpVariable("NumIJ10k", lowBound=0, cat='Integer')
num_ij_3k = LpVariable("NumIJ3k", lowBound=0, cat='Integer')
num_ij_2500 = LpVariable("NumIJ2500", lowBound=0, cat='Integer')
num_fs_8k = LpVariable("NumFS8k", lowBound=0, cat='Integer')
num_fs_6k = LpVariable("NumFS6k", lowBound=0, cat='Integer')
num_fs_2k = LpVariable("NumFS2k", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("DorianAutoProblem", LpMaximize)

# Define the objective function
objective = 10000 * num_ij_10k + 3000 * num_ij_3k + 2500 * num_ij_2500 + 8000 * num_fs_8k + 6000 * num_fs_6k + 2000 * num_fs_2k
problem += objective

# Define the constraints
problem += 1000 * (num_ij_10k + num_ij_3k + num_ij_2500 + num_fs_8k + num_fs_6k + num_fs_2k) <= 20000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of IJ ads yielding 10,000 exposures:", value(num_ij_10k))
print("The number of IJ ads yielding 3,000 exposures:", value(num_ij_3k))
print("The number of IJ ads yielding 2,500 exposures:", value(num_ij_2500))
print("The number of FS ads yielding 8,000 exposures:", value(num_fs_8k))
print("The number of FS ads yielding 6,000 exposures:", value(num_fs_6k))
print("The number of FS ads yielding 2,000 exposures:", value(num_fs_2k))
print("The maximum number of exposures:", value(objective))
print("## end solving")