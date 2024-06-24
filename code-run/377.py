from pulp import *

# Define the variables
num_IJ_10k = LpVariable("NumIJ10k", lowBound=0, cat='Integer')
num_IJ_3k = LpVariable("NumIJ3k", lowBound=0, cat='Integer')
num_IJ_2k5 = LpVariable("NumIJ2k5", lowBound=0, cat='Integer')
num_FS_8k = LpVariable("NumFS8k", lowBound=0, cat='Integer')
num_FS_6k = LpVariable("NumFS6k", lowBound=0, cat='Integer')
num_FS_2k = LpVariable("NumFS2k", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("DorianAutoProblem", LpMaximize)

# Define the objective function
objective = 10000 * num_IJ_10k + 3000 * num_IJ_3k + 2500 * num_IJ_2k5 + 8000 * num_FS_8k + 6000 * num_FS_6k + 2000 * num_FS_2k
problem += objective

# Define the constraints
problem += 1000 * (num_IJ_10k + num_IJ_3k + num_IJ_2k5 + num_FS_8k + num_FS_6k + num_FS_2k) <= 20000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of IJ ads yielding 10,000 exposures:", num_IJ_10k.value())
print("The number of IJ ads yielding 3,000 exposures:", num_IJ_3k.value())
print("The number of IJ ads yielding 2,500 exposures:", num_IJ_2k5.value())
print("The number of FS ads yielding 8,000 exposures:", num_FS_8k.value())
print("The number of FS ads yielding 6,000 exposures:", num_FS_6k.value())
print("The number of FS ads yielding 2,000 exposures:", num_FS_2k.value())
print("The maximum number of exposures:", objective.value())
print("## end solving")