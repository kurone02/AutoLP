from pulp import *

# Define the variables
num_ads_IJ_10000 = LpVariable("num_ads_IJ_10000", lowBound=0, cat='Integer')
num_ads_IJ_3000 = LpVariable("num_ads_IJ_3000", lowBound=0, cat='Integer')
num_ads_IJ_2500 = LpVariable("num_ads_IJ_2500", lowBound=0, cat='Integer')
num_ads_FS_8000 = LpVariable("num_ads_FS_8000", lowBound=0, cat='Integer')
num_ads_FS_6000 = LpVariable("num_ads_FS_6000", lowBound=0, cat='Integer')
num_ads_FS_2000 = LpVariable("num_ads_FS_2000", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("DorianAutoProblem", LpMaximize)

# Define the objective function
problem += 10000 * num_ads_IJ_10000 + 3000 * num_ads_IJ_3000 + 2500 * num_ads_IJ_2500 + 8000 * num_ads_FS_8000 + 6000 * num_ads_FS_6000 + 2000 * num_ads_FS_2000

# Define the constraints
problem += 1000 * (num_ads_IJ_10000 + num_ads_IJ_3000 + num_ads_IJ_2500 + num_ads_FS_8000 + num_ads_FS_6000 + num_ads_FS_2000) <= 20000
problem += num_ads_IJ_10000 + num_ads_IJ_3000 + num_ads_IJ_2500 <= 15
problem += num_ads_FS_8000 + num_ads_FS_6000 + num_ads_FS_2000 <= 12

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of ads in IJ yielding 10,000 exposures:", num_ads_IJ_10000.value())
print("The number of ads in IJ yielding 3,000 exposures:", num_ads_IJ_3000.value())
print("The number of ads in IJ yielding 2,500 exposures:", num_ads_IJ_2500.value())
print("The number of ads in FS yielding 8,000 exposures:", num_ads_FS_8000.value())
print("The number of ads in FS yielding 6,000 exposures:", num_ads_FS_6000.value())
print("The number of ads in FS yielding 2,000 exposures:", num_ads_FS_2000.value())
print("The maximum number of exposures:", problem.objective.value())
print("## end solving")