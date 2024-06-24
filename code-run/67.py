from pulp import *

# Define the decision variables
# number of coats
num_coats = LpVariable("NumCoats", lowBound=0, cat='Integer')
# number of skirts
num_skirts = LpVariable("NumSkirts", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("XLuxuryClothProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 12 * num_coats + 16 * num_skirts
problem += objective

# Define the constraints
# total designing time
problem += 1.5 * num_coats + 3 * num_skirts <= 45
# total printing time
problem += 2.5 * num_coats + 3.5 * num_skirts <= 70

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of coats:", num_coats.value())
print("The number of skirts:", num_skirts.value())
print("The total profit:", objective.value())
print("## end solving")