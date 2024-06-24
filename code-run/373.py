from pulp import *

# Define the decision variables
num_classic = LpVariable("NumClassic", lowBound=0, cat='Integer')
num_modern = LpVariable("NumModern", lowBound=0, cat='Integer') 

# Define the problem
problem = LpProblem("RFCOverheadProblem", LpMaximize)

# Define the objective function
objective = (310 * num_classic + 350 * num_modern) - (1.50 * 90 * num_classic + 1.50 * 100 * num_modern + 2 * 50 * num_classic + 2 * 60 * num_modern)
problem += objective

# Define the constraints
problem += num_classic + num_modern <= 20 + 25
problem += 1.20 * num_classic + 0.90 * num_modern <= 40
problem += 1.00 * num_classic + 1.20 * num_modern <= 40
problem += 90 * num_classic + 100 * num_modern <= 2000
problem += 50 * num_classic + 60 * num_modern <= 1500

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of Classic dressers to produce:", num_classic.value())
print("The number of Modern dressers to produce:", num_modern.value())
print("The maximum contribution to overhead:", objective.value())
print("## end solving")