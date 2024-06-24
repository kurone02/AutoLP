from pulp import *

# Define the decision variables
# number of chocolate crepes
num_choco_crepes = LpVariable("NumChocoCrepes", lowBound=0, cat='Integer')
# number of peanut butter crepes
num_peanut_crepes = LpVariable("NumPeanutCrepes", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("CrepeStoreProblem", LpMinimize)

# Define the objective function
# minimize the total amount of crepe mix needed
objective = 6 * num_choco_crepes + 7 * num_peanut_crepes
problem += objective

# Define the constraints
# chocolate crepe constraint
problem += num_choco_crepes >= 0.25 * (num_choco_crepes + num_peanut_crepes)
# peanut butter crepe constraint
problem += num_peanut_crepes >= num_choco_crepes
# spread constraint
problem += 3 * num_choco_crepes + 4 * num_peanut_crepes <= 400

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of chocolate crepes:", num_choco_crepes.value())
print("The number of peanut butter crepes:", num_peanut_crepes.value())
print("The amount of crepe mix used:", objective.value())
print("## end solving")